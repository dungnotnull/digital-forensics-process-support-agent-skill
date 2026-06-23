# PROJECT-detail.md — Digital Forensics Process Support (evidence integrity)

## Executive Summary
`digital-forensics-process-support` turns Claude into a certified digital forensics examiner and expert witness who audits investigative procedures for court admissibility. It runs a research-first harness that intakes the user's case, binds it to named world-renowned frameworks, scores it on 8 dimensions, and returns a prioritized improvement roadmap with effort/impact. The skill is self-improving: `tools/knowledge_updater.py` continuously refreshes its knowledge base from authoritative sources.

## Problem Statement
Investigators, IT teams, and legal staff need to confirm that their acquisition, analysis, and preservation steps will hold up legally — broken chain-of-custody or unsound imaging can void evidence.

## Target Users & Use Cases
- Primary: practitioners and non-experts who need an expert-grade, evidence-based assessment of their digital forensics process support (evidence integrity) artifact.
- Trigger examples:
  - User says: "Disk image acquisition" → skill flag broken acquisition soundness, score integrity low, roadmap to re-acquire with validated tooling
  - User says: "Chain-of-custody gap" → skill flag chain-of-custody failure, admissibility risk, documentation roadmap
  - User says: "Hash verification" → skill verify integrity, score reproducibility, note md5 weakness vs sha-256

## Harness Architecture
```
intake/requirements
    │  requirements-gatherer → risk-screener → compliance-check → scoring-engine → improvement-roadmap → synthesis
    ▼
[named frameworks] → [multi-dimensional scoring] → [prioritized roadmap] → [quality/compliance gates] → DELIVERABLE
```

## Evaluation Frameworks (world-renowned, citable)
- **ISO/IEC 27037 (identification, collection, acquisition, preservation)** — International standard for digital evidence handling
- **NIST SP 800-86 (forensic techniques into incident response)** — Process model for forensic investigation
- **ACPO Good Practice Guide for Digital Evidence** — Four principles of digital evidence handling
- **Daubert/Frye admissibility standards** — Legal admissibility of scientific evidence
- **SWGDE Best Practices** — Scientific Working Group on Digital Evidence procedures

## Scoring Dimensions
1. Identification & scoping
2. Acquisition soundness (write-blocking, imaging)
3. Hash verification & integrity
4. Chain-of-custody documentation
5. Analysis reproducibility
6. Tool validation
7. Reporting & admissibility
8. Privacy/legal authority

## Full Sub-Skill Catalog
### `sub-requirements-gatherer`
- **Purpose:** Capture objectives, stakeholders, constraints, and the document/artifact under review so analysis is complete.
- **Inputs:** User brief, uploaded documents, clarifying answers
- **Outputs:** Structured requirements pack with scope, stakeholders, and explicit out-of-scope items
- **Tools:** Read, WebSearch
- **Quality gate:** Scope, stakeholders, and success criteria all captured; ambiguities flagged for confirmation.
### `sub-risk-screener`
- **Purpose:** Surface the highest-impact risks early so the analysis and roadmap focus where it matters.
- **Inputs:** Structured requirements / artifact
- **Outputs:** Ranked risk register (likelihood x impact) with the specific evidence for each risk
- **Tools:** Read, WebSearch
- **Quality gate:** Each risk has likelihood, impact, and a cited or quoted evidence anchor.
### `sub-compliance-check`
- **Purpose:** Ensure no output crosses into unauthorized practice or non-compliant claims; attach required disclaimers and jurisdiction notes.
- **Inputs:** Draft deliverable, jurisdiction, domain
- **Outputs:** Compliance verdict, required disclaimers, and a list of any claims that must be softened or removed
- **Tools:** Read, WebSearch, WebFetch
- **Quality gate:** Jurisdiction identified; mandatory disclaimers attached; no statement presented as a substitute for licensed professional advice.
### `sub-scoring-engine`
- **Purpose:** Produce a transparent, dimension-by-dimension score (0-100 or band) with evidence for every sub-score.
- **Inputs:** Normalized profile, selected framework + rubric
- **Outputs:** Per-dimension scores, weighted total, strengths, and ranked weaknesses each tied to evidence
- **Tools:** Read, WebSearch
- **Quality gate:** Every dimension has a numeric score AND a one-line evidence/justification; no unscored dimension.
### `sub-improvement-roadmap`
- **Purpose:** Convert weaknesses into a sequenced, effort/impact-ranked action plan the user can execute.
- **Inputs:** Scored weaknesses, user constraints
- **Outputs:** Prioritized roadmap (Quick wins / Major projects / Long-term) with effort, impact, and success metric per item
- **Tools:** Read, Write
- **Quality gate:** Every recommendation has effort, impact, and a measurable success criterion.

## Skill File Format Specification
Each skill file uses YAML frontmatter (`name`, `description`) followed by: Role & Persona, Workflow (Harness Flow), Sub-skills Available, Tools, Output Format, Quality Gates. `skills/main.md` is the harness entry point and invokes the sub-skills above in order.

## E2E Execution Flow
1. Parse the user request and uploaded artifact(s).
2. Run intake/requirements sub-skill; flag unknowns (no silent assumptions).
3. (No safety gate for this cluster.)
4. Select governing framework(s) and rubric.
5. Score every dimension with cited evidence.
6. Generate the prioritized roadmap (effort/impact + success metric).
7. Run sub-compliance-check; attach disclaimers/jurisdiction notes before output.
8. Synthesize the final professional deliverable; pass all quality gates before display.

## SECOND-KNOWLEDGE-BRAIN Integration
- Sources: NIST Computer Forensics, ISO/IEC 27037, SWGDE, DFIR community resources
- ArXiv categories: cs.CR
- Search queries: "digital forensics chain of custody", "evidence integrity hashing admissibility", "incident response forensic acquisition"
- Append format: dated entries with Title, Authors, Year, Venue, DOI/Link, Relevance.

## Supporting Tools Spec
`tools/knowledge_updater.py`: crawl4ai → fetch → parse → score (recency × relevance) → dedupe (URL/DOI hash) → append to `SECOND-KNOWLEDGE-BRAIN.md`. Schedule: weekly cron.

## Quality Gates (must all pass before output)
- Every scored dimension has evidence.
- At least one named framework cited.
- Roadmap items each have effort, impact, and a measurable success metric.
- Compliance check passed with disclaimers attached.

## Test Scenarios
1. **Disk image acquisition** — Input: Investigator describes imaging a suspect drive without a write-blocker → Expected: Flag broken acquisition soundness, score integrity low, roadmap to re-acquire with validated tooling
2. **Chain-of-custody gap** — Input: Evidence handled by multiple staff with no log → Expected: Flag chain-of-custody failure, admissibility risk, documentation roadmap
3. **Hash verification** — Input: Examiner provides MD5/SHA hashes pre/post analysis → Expected: Verify integrity, score reproducibility, note MD5 weakness vs SHA-256
4. **Cloud evidence** — Input: Investigator needs to collect from a SaaS account → Expected: Legal-authority check, ISO 27037 acquisition guidance, compliance disclaimers
5. **Tool validation** — Input: Examiner uses an unvalidated custom script → Expected: Flag tool-validation gap (NIST CFTT), recommend validated alternatives

## Key Design Decisions
1. Scoring is always bound to named, citable frameworks — never ad hoc.
2. Intake forbids silent assumptions; unknowns are surfaced.
3. Roadmap is effort/impact-ranked and measurable.
4. Knowledge base is self-updating for trend alignment.
5. Safety/compliance gating is mandatory and blocking.
