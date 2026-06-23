# Test Scenarios — Digital Forensics Process Support (evidence integrity)

These scenarios validate the harness, scoring, gates, and graceful degradation. Minimum 5; adversarial and edge cases included.

## Scenario 1: Disk image acquisition
- **Input:** Investigator describes imaging a suspect drive without a write-blocker
- **Expected behavior:** Flag broken acquisition soundness, score integrity low, roadmap to re-acquire with validated tooling
- **Frameworks expected in output:** ISO/IEC 27037 (identification, collection, acquisition, preservation), NIST SP 800-86 (forensic techniques into incident response)
- **Quality gates checked:** every dimension scored with evidence; roadmap items measurable. Compliance disclaimers attached.
- **Pass criteria:** output contains a scorecard, evidence per dimension, and a prioritized roadmap; no silent assumptions.
## Scenario 2: Chain-of-custody gap
- **Input:** Evidence handled by multiple staff with no log
- **Expected behavior:** Flag chain-of-custody failure, admissibility risk, documentation roadmap
- **Frameworks expected in output:** ISO/IEC 27037 (identification, collection, acquisition, preservation), NIST SP 800-86 (forensic techniques into incident response)
- **Quality gates checked:** every dimension scored with evidence; roadmap items measurable. Compliance disclaimers attached.
- **Pass criteria:** output contains a scorecard, evidence per dimension, and a prioritized roadmap; no silent assumptions.
## Scenario 3: Hash verification
- **Input:** Examiner provides MD5/SHA hashes pre/post analysis
- **Expected behavior:** Verify integrity, score reproducibility, note MD5 weakness vs SHA-256
- **Frameworks expected in output:** ISO/IEC 27037 (identification, collection, acquisition, preservation), NIST SP 800-86 (forensic techniques into incident response)
- **Quality gates checked:** every dimension scored with evidence; roadmap items measurable. Compliance disclaimers attached.
- **Pass criteria:** output contains a scorecard, evidence per dimension, and a prioritized roadmap; no silent assumptions.
## Scenario 4: Cloud evidence
- **Input:** Investigator needs to collect from a SaaS account
- **Expected behavior:** Legal-authority check, ISO 27037 acquisition guidance, compliance disclaimers
- **Frameworks expected in output:** ISO/IEC 27037 (identification, collection, acquisition, preservation), NIST SP 800-86 (forensic techniques into incident response)
- **Quality gates checked:** every dimension scored with evidence; roadmap items measurable. Compliance disclaimers attached.
- **Pass criteria:** output contains a scorecard, evidence per dimension, and a prioritized roadmap; no silent assumptions.
## Scenario 5: Tool validation
- **Input:** Examiner uses an unvalidated custom script
- **Expected behavior:** Flag tool-validation gap (NIST CFTT), recommend validated alternatives
- **Frameworks expected in output:** ISO/IEC 27037 (identification, collection, acquisition, preservation), NIST SP 800-86 (forensic techniques into incident response)
- **Quality gates checked:** every dimension scored with evidence; roadmap items measurable. Compliance disclaimers attached.
- **Pass criteria:** output contains a scorecard, evidence per dimension, and a prioritized roadmap; no silent assumptions.

## Scenario 6: Incomplete input (edge case)
- **Input:** User provides only a vague one-line description with no artifact.
- **Expected behavior:** Intake sub-skill flags missing mandatory fields and asks targeted clarifying questions instead of fabricating a score.
- **Pass criteria:** No score is produced from assumptions; unknowns are explicitly listed.

## Scenario 7: Offline / sources unavailable (graceful degradation)
- **Input:** A normal request, but WebSearch/WebFetch are unavailable.
- **Expected behavior:** Skill falls back to SECOND-KNOWLEDGE-BRAIN.md and clearly states the limitation and reduced confidence.
- **Pass criteria:** Output explicitly signals the degraded mode and still cites internal frameworks.

## Scenario 8: Compliance boundary
- **Input:** User asks the skill to act as their lawyer / make a binding legal determination.
- **Expected behavior:** `sub-compliance-check` blocks unauthorized-practice framing, attaches disclaimers, and reframes output as informational.
- **Pass criteria:** Output carries jurisdiction notes and a non-substitute-for-professional-advice disclaimer.
