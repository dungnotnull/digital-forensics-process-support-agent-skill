# CLAUDE.md — Digital Forensics Process Support (evidence integrity)

**Skill name:** `digital-forensics-process-support`
**Tagline:** Evaluate a digital-forensics process for evidence integrity, chain-of-custody, and legal admissibility.
**Source idea:** #90 (cluster: `legal-compliance`)
**Current phase:** Phase 4 — Testing & Validation (initial build complete)

## Problem This Skill Solves
Investigators, IT teams, and legal staff need to confirm that their acquisition, analysis, and preservation steps will hold up legally — broken chain-of-custody or unsound imaging can void evidence.

## Harness Flow Summary
1. **sub-requirements-gatherer** → Capture objectives, stakeholders, constraints, and the document/artifact under review so analysis is complete.
2. **sub-risk-screener** → Surface the highest-impact risks early so the analysis and roadmap focus where it matters.
3. **sub-compliance-check** → Ensure no output crosses into unauthorized practice or non-compliant claims; attach required disclaimers and jurisdiction notes.
4. **sub-scoring-engine** → Produce a transparent, dimension-by-dimension score (0-100 or band) with evidence for every sub-score.
5. **sub-improvement-roadmap** → Convert weaknesses into a sequenced, effort/impact-ranked action plan the user can execute.
6. **main (synthesis)** → assemble the scored deliverable + prioritized roadmap and run final quality gates.

## Gates
**Compliance gate:** `sub-compliance-check` MUST run before the final deliverable is emitted. Attach jurisdiction notes and required disclaimers; never present output as a substitute for licensed professional advice.

## Sub-skills
- `skills/sub-requirements-gatherer.md` — Elicit and structure the full set of forensic investigation requirements and context.
- `skills/sub-risk-screener.md` — Identify and rank evidence-integrity risks and red-flag clauses/conditions.
- `skills/sub-compliance-check.md` — Verify the deliverable against applicable laws, standards, and disclosure rules.
- `skills/sub-scoring-engine.md` — Multi-dimensional scoring of the forensic process against the selected framework.
- `skills/sub-improvement-roadmap.md` — Prioritized improvement roadmap for the forensic process with effort/impact.

## Tools Required
WebSearch, WebFetch, Read, Write, Bash

## Knowledge Sources
- [NIST Computer Forensics](https://www.nist.gov/itl/ssd/software-quality-group/computer-forensics-tool-testing-program-cftt)
- [ISO/IEC 27037](https://www.iso.org/standard/44381.html)
- [SWGDE](https://www.swgde.org)
- [DFIR community resources](https://www.forensicfocus.com)

ArXiv / research categories crawled: cs.CR

## Supporting Tools
- `tools/knowledge_updater.py` — crawl4ai pipeline that refreshes `SECOND-KNOWLEDGE-BRAIN.md` weekly from the sources above.

## Active Development Tasks
- [x] Scaffold deliverables and sub-skills
- [x] Define scoring dimensions against named frameworks
- [ ] Expand `SECOND-KNOWLEDGE-BRAIN.md` with first crawl batch
- [ ] Add 3 more adversarial test scenarios
- [ ] Wire shared cluster sub-skills for reuse

## Reference Docs
- `PROJECT-detail.md` — full technical spec
- `PROJECT-DEVELOPMENT-PHASE-TRACKING.md` — phase roadmap
- `SECOND-KNOWLEDGE-BRAIN.md` — living domain knowledge base
