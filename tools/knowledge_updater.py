# -*- coding: utf-8 -*-
"""knowledge_updater.py — self-improving crawler for the Digital Forensics Process Support (evidence integrity) skill.

Pipeline (see CLAUDE.md SECOND-KNOWLEDGE-BRAIN architecture):
  1. crawl4ai -> fetch latest papers/docs from domain sources
  2. WebSearch-style queries -> latest news/reports
  3. parse -> title, authors, date, DOI/URL, abstract, key findings
  4. score -> recency * domain-keyword relevance
  5. append -> add scored entries to SECOND-KNOWLEDGE-BRAIN.md
  6. dedupe -> skip entries already present (URL/DOI hash)

Run weekly (cron). Requires: pip install crawl4ai
"""
import os, re, json, hashlib, datetime

SKILL_ID = 90
SKILL_SLUG = "digital-forensics-process-support"
BRAIN = os.path.join(os.path.dirname(__file__), "..", "SECOND-KNOWLEDGE-BRAIN.md")

ARXIV_CATEGORIES = ["cs.CR"]
SEARCH_QUERIES = ["digital forensics chain of custody", "evidence integrity hashing admissibility", "incident response forensic acquisition"]
SOURCE_URLS = ["https://www.nist.gov/itl/ssd/software-quality-group/computer-forensics-tool-testing-program-cftt", "https://www.iso.org/standard/44381.html", "https://www.swgde.org", "https://www.forensicfocus.com"]
DOMAIN_KEYWORDS = ["digital forensics chain of custody", "evidence integrity hashing admissibility", "incident response forensic acquisition"]


def _hash(url):
    return hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]


def load_seen_hashes():
    if not os.path.exists(BRAIN):
        return set()
    with open(BRAIN, "r", encoding="utf-8") as f:
        text = f.read()
    return set(re.findall(r"<!--hash:([0-9a-f]{16})-->", text))


def relevance_score(entry):
    """recency (0-1) * keyword-match (0-1)."""
    try:
        year = int(entry.get("year", 0))
    except (TypeError, ValueError):
        year = 0
    now = datetime.date.today().year
    recency = max(0.0, 1.0 - (now - year) / 8.0) if year else 0.3
    text = (entry.get("title", "") + " " + entry.get("abstract", "")).lower()
    hits = sum(1 for kw in DOMAIN_KEYWORDS if kw.lower() in text)
    rel = min(1.0, hits / max(1, len(DOMAIN_KEYWORDS)))
    return round(recency * (0.4 + 0.6 * rel), 3)


def fetch_entries():
    """Fetch candidate entries via crawl4ai. Returns list of dicts.

    Network/crawl4ai calls are wrapped defensively: on any failure the skill
    degrades gracefully (returns []) and the harness falls back to the existing
    knowledge base, per Design Principle 8 (graceful degradation).
    """
    entries = []
    try:
        from crawl4ai import WebCrawler  # type: ignore
        crawler = WebCrawler()
        crawler.warmup()
        for cat in ARXIV_CATEGORIES:
            url = "https://arxiv.org/list/%s/recent" % cat
            try:
                res = crawler.run(url=url)
                entries.extend(_parse_arxiv(getattr(res, "markdown", "") or ""))
            except Exception as e:
                print("[warn] arxiv %s failed: %s" % (cat, e))
        for url in SOURCE_URLS:
            try:
                res = crawler.run(url=url)
                entries.append({"title": "Source scan: %s" % url,
                                "url": url, "year": datetime.date.today().year,
                                "authors": "", "abstract": getattr(res, "markdown", "")[:500]})
            except Exception as e:
                print("[warn] source %s failed: %s" % (url, e))
    except Exception as e:
        print("[warn] crawl4ai unavailable (%s); skipping live crawl." % e)
    return entries


def _parse_arxiv(md):
    out = []
    for m in re.finditer(r"arXiv:(\d+\.\d+)", md or ""):
        aid = m.group(1)
        out.append({"title": "arXiv:%s" % aid, "url": "https://arxiv.org/abs/%s" % aid,
                     "authors": "", "year": datetime.date.today().year, "abstract": ""})
    return out


def append_entries(entries):
    seen = load_seen_hashes()
    scored = sorted(((relevance_score(e), e) for e in entries), reverse=True,
                    key=lambda x: x[0])
    today = datetime.date.today().isoformat()
    new_blocks = []
    for score, e in scored:
        url = e.get("url", "")
        if not url:
            continue
        h = _hash(url)
        if h in seen:
            continue
        seen.add(h)
        new_blocks.append(
            "### [%s] %s\n- Authors: %s\n- Year: %s\n- Link: %s\n- Relevance score: %s\n- Key findings: %s\n<!--hash:%s-->\n" % (
                today, e.get("title", "Untitled"), e.get("authors", "n/a"),
                e.get("year", "n/a"), url, score,
                (e.get("abstract", "") or "(abstract pending)")[:280], h))
    if not new_blocks:
        print("No new entries to append.")
        return
    with open(BRAIN, "a", encoding="utf-8") as f:
        f.write("\n\n## Automated Crawl Batch — %s\n\n" % today)
        f.write("\n".join(new_blocks))
    print("Appended %d new entries." % len(new_blocks))


def main():
    print("[knowledge_updater] skill #%s (%s)" % (SKILL_ID, SKILL_SLUG))
    entries = fetch_entries()
    print("Fetched %d candidate entries." % len(entries))
    append_entries(entries)


if __name__ == "__main__":
    main()
