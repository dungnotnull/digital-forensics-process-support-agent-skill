# SECOND-KNOWLEDGE-BRAIN.md — Digital Forensics Process Support (evidence integrity)

> Living, self-improving knowledge base. Grown weekly by `tools/knowledge_updater.py`.
> Last automated crawl: 2026-06-18

## Table of Contents
1. [Core Concepts & Frameworks](#1-core-concepts--frameworks)
2. [Detailed Framework Specifications](#2-detailed-framework-specifications)
3. [Scoring Dimensions & Rubrics](#3-scoring-dimensions--rubrics)
4. [Key Research Papers](#4-key-research-papers)
5. [State-of-the-Art Methods & Tools](#5-state-of-the-art-methods--tools)
6. [Authoritative Data Sources](#6-authoritative-data-sources)
7. [Compliance & Legal Standards](#7-compliance--legal-standards)
8. [Quality Checkpoints](#8-quality-checkpoints)
9. [Knowledge Update Log](#9-knowledge-update-log)

---

## 1. Core Concepts & Frameworks

### Primary Frameworks (World-Renowned, Citable)

| Framework | Year | Focus Area | Authority Level |
|-----------|------|------------|-----------------|
| **ISO/IEC 27037:2012** | 2012 | Identification, collection, acquisition, preservation of digital evidence | International Standard |
| **NIST SP 800-86** | 2006 | Integrating forensic techniques into incident response | US National Standard |
| **ACPO Good Practice Guide** | 2012 | Four principles of digital evidence handling | UK Police Guidelines |
| **SWGDE Best Practices** | 2025 | Scientific Working Group procedures | Scientific Consensus |
| **Daubert/Frye Standards** | 1993 | Legal admissibility of scientific evidence | US Supreme Court/State Standards |

---

## 2. Detailed Framework Specifications

### 2.1 ISO/IEC 27037:2012 - Information Technology Security Techniques

**Current Status**: The 2012 edition remains the active standard. A revision was opened in 2024 but not yet published.

**Core Activities**:

1. **Identification**
   - Recognizing and defining potential digital evidence
   - Assessing evidentiary value
   - Determining scope of collection
   - Documentation of evidence type and source

2. **Collection**
   - Procedures for seizing digital evidence
   - Maintaining chain of custody documentation
   - Documenting the collection process
   - Evidence bagging and labeling protocols

3. **Acquisition**
   - Creating forensic images using write-blocked hardware
   - Generating verified hash values pre/post acquisition
   - Ensuring data integrity during copying
   - Bit-by-bit imaging requirements
   - Handling volatile evidence (RAM, network data)

4. **Preservation**
   - Proper storage conditions (temperature, humidity, ESD protection)
   - Maintaining evidentiary integrity through hash verification
   - Preventing data contamination or alteration
   - Long-term archival considerations

**Evidence Types Covered**:
- Hard drives and solid-state storage
- Mobile devices and smartphones
- Volatile evidence (RAM, running processes, network connections)
- Cloud-based evidence (SaaS, IaaS, PaaS)
- Electronic records and metadata
- IoT devices and embedded systems

**Key Principles**:
- **Chain of custody**: Continuous documentation from collection to court
- **Data integrity**: Cryptographic hash verification (SHA-256 recommended)
- **Minimal alteration**: Non-invasive acquisition methods
- **Comprehensive documentation**: Every action recorded and justifiable
- **Traceability**: Complete audit trail of evidence handling

**Related Standards in Series**:
- ISO/IEC 27041: Incident investigation principles
- ISO/IEC 27042: Digital evidence analysis interpretation
- ISO/IEC 27043: Investigation principles
- ISO/IEC 27050: Electronic discovery

**Sources**:
- [ISO/IEC 27037:2012 Official Standard](https://www.iso.org/standard/44381.html)
- [Digital Evidence Preservation: Standards Compared - TrueScreen](https://truescreen.io/articles/digital-evidence-preservation-standards/)
- [ISO/IEC 27037: Understanding its role in compliance and security](https://www.konfirmity.com/glossary/iso-iec-27037)
- [An Empirical Assessment of Digital Forensic Process Reliability](https://www.mdpi.com/2624-800X/6/2/57)

---

### 2.2 NIST SP 800-86 - Guide to Integrating Forensic Techniques into Incident Response

**Publication Details**:
- **Publisher**: National Institute of Standards and Technology (NIST)
- **Document Type**: Special Publication 800-86
- **Purpose**: Guidelines for incorporating digital forensic methods into cybersecurity incident response
- **Status**: Active reference document

**Core Focus Areas**:

1. **Bridge Between Disciplines**
   - Integrates technical forensic skills with incident response
   - Addresses legal compliance requirements
   - Aligns investigative methodology with operational needs

2. **Incident Response Integration**
   - When to apply forensic techniques
   - How to preserve evidence during response
   - Balancing response speed with evidence preservation

3. **Investigative Process Model**
   - Preparation phase: tools, training, procedures
   - Detection and analysis phases
   - Containment, eradication, and recovery
   - Post-incident activity and lessons learned

4. **Evidence Handling Throughout IR Lifecycle**
   - Initial triage and volatile data capture
   - System imaging and evidence acquisition
   - Analysis while maintaining evidentiary value
   - Reporting and legal considerations

**Key Integration Points**:
- Referenced by NIST SP 800-61 (Computer Security Incident Handling Guide)
- Used in cybersecurity training and certification exams
- Applicable beyond security incidents to IT operational issues
- Emphasizes maintaining legal admissibility while responding

**Sources**:
- [NIST CSRC: Guide to Integrating Forensic Techniques into Incident Response](https://csrc.nist.gov/pubs/sp/800/86/final)
- [Official PDF Document](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-86.pdf)

---

### 2.3 ACPO Good Practice Guide for Digital Evidence

**Status**: Primary UK standard for digital evidence handling

**Four Principles of Digital Evidence**:

1. **Principle 1: Data Integrity**
   - No action taken should change data
   - Any changes must be documented and justified
   - Original evidence must be preserved whenever possible

2. **Principle 2: Competence**
   - Person accessing data must be competent to do so
   - Training and certification requirements
   - Understanding of tools and their limitations

3. **Principle 3: Audit Trail**
   - Complete record of all actions taken
   - Chain of custody documentation
   - Process documentation and justification

4. **Principle 4: Compliance**
   - Adherence to laws and organizational policies
   - Understanding of legal requirements
   - Regular review and update of procedures

**Practical Application**:
- Standard for UK law enforcement digital investigations
- Adopted by many international organizations
- Foundation for evidence handling policies
- Basis for training and certification programs

---

### 2.4 SWGDE Best Practices (2025 Update)

**Current Status**: Active updates through 2025

**Key 2025 Publications**:

1. **Best Practices for Digital Evidence Collection v2.0** (June 30, 2025)
   - Updated collection protocols
   - Cloud evidence considerations
   - Remote collection procedures
   - [PDF Document](https://www.swgde.org/wp-content/uploads/2025/07/2025-06-30-Best-Practices-for-Digital-Evidence-Collection-18-F-002-2.0.pdf)

2. **Best Practices for Mobile Device Evidence v2.0** (February 28, 2025)
   - Mobile device acquisition standards
   - Preservation of mobile evidence
   - Handling and acquisition protocols

3. **Best Practices for Digital Forensic Video Analysis v2.0** (December 10, 2025)
   - Video evidence analysis
   - Authentication procedures
   - Presentation standards

4. **Best Practices for Maintaining Imagery Integrity v1.1** (March 3, 2025)
   - Image evidence authentication
   - Integrity verification methods
   - Format considerations

**SWGDE Process**:
- Consensus-based development with subject matter experts
- Regular review and update cycle
- Multi-organizational input and validation
- Public comment periods

**Sources**:
- [SWGDE Documents - Complete Listing](https://www.swgde.org/documents/published-complete-listing/18-f-002-best-practices-for-digital-evidence-collection/)
- [SWGDE Forensics Documents Page](https://www.swgde.org/documents/published-by-committee/forensics/)

---

### 2.5 Daubert/Frye Admissibility Standards

**Daubert Standard (Federal)**:
- Supreme Court ruling: *Daubert v. Merrell Dow Pharmaceuticals, 1993*
- Criteria for scientific evidence admissibility:
  1. Testability: Can the theory be tested?
  2. Peer Review: Has it been published and reviewed?
  3. Error Rate: Known or potential error rate
  4. Standards: Existence of controlling standards
  5. Acceptance: General acceptance in scientific community

**Frye Standard (State-Level)**:
- *Frye v. United States, 1923*
- "General acceptance" test
- Scientific principle must be "sufficiently established"
- Used in several state jurisdictions

**Implications for Digital Forensics**:
- Tool validation requirements (NIST CFTT)
- Method repeatability and documentation
- Expert witness qualifications
- Error rate documentation for tools used
- Peer review of forensic methods

---

## 3. Scoring Dimensions & Rubrics

### Scoring Framework (0-100 Scale)

Each dimension is scored based on alignment with the frameworks above. Scores are evidence-based and tied to specific framework citations.

#### Dimension 1: Identification & Scoping (15 points)

| Score Range | Criteria | Framework Reference |
|-------------|----------|-------------------|
| 13-15 | Comprehensive evidence inventory, clear scope definition, all sources identified | ISO 27037 §5, NIST 800-86 §3.1 |
| 10-12 | Good evidence identification, minor scope gaps, most sources documented | ISO 27037 §5 |
| 7-9 | Basic identification, significant scope questions, incomplete source listing | - |
| 0-6 | Poor or no evidence identification, unclear scope, critical gaps | - |

**Key Assessment Points**:
- Are all relevant digital assets identified?
- Is the investigation scope clearly defined?
- Are potential evidence sources documented?
- Is the evidentiary value assessed?

---

#### Dimension 2: Acquisition Soundness (15 points)

| Score Range | Criteria | Framework Reference |
|-------------|----------|-------------------|
| 13-15 | Write-blocker used, bit-by-bit imaging, hash verification, proper tooling | ISO 27037 §6, SWGDE Collection v2.0 |
| 10-12 | Appropriate imaging methods, hash verification, minor documentation gaps | ISO 27037 §6 |
| 7-9 | Basic acquisition, questionable write-blocking, incomplete verification | - |
| 0-6 | Improper acquisition, no write-blocking, no verification, potential evidence alteration | - |

**Critical Elements**:
- Hardware or software write-blocker used
- Bit-by-bit forensic imaging performed
- Hash values calculated pre/post acquisition
- Acquisition tools validated (NIST CFTT)
- Proper handling of volatile evidence

---

#### Dimension 3: Hash Verification & Integrity (15 points)

| Score Range | Criteria | Framework Reference |
|-------------|----------|-------------------|
| 13-15 | SHA-256 or better, verified throughout chain, documented, secure storage | ISO 27037 §6.3, NIST 800-86 §4 |
| 10-12 | Strong hashing (SHA-1+), documented verification, good chain | ISO 27037 §6.3 |
| 7-9 | MD5 only, some verification, incomplete documentation | - |
| 0-6 | Weak or no hashing, MD5 only without justification, no verification chain | - |

**Hash Standards**:
- **Recommended**: SHA-256, SHA-384, SHA-512
- **Acceptable**: SHA-1 with documented risk assessment
- **Deprecated**: MD5 (only with justification of legacy requirements)
- **Verification required**: Pre-acquisition, post-acquisition, post-analysis

---

#### Dimension 4: Chain-of-Custody Documentation (15 points)

| Score Range | Criteria | Framework Reference |
|-------------|----------|-------------------|
| 13-15 | Continuous documentation, all handlers logged, timestamps, no gaps | ISO 27037 §7, ACPO Principle 3 |
| 10-12 | Good documentation, minor gaps, most transfers logged | ISO 27037 §7 |
| 7-9 | Basic logging, significant gaps, unclear handler sequence | - |
| 0-6 | Poor or no chain-of-custody, critical gaps, evidence integrity compromised | - |

**Required Documentation**:
- Evidence collection details (who, when, where, how)
- Complete transfer history
- Each handler's identity and role
- Timestamps for all custody changes
- Storage location and condition records
- Access logs and authorization

---

#### Dimension 5: Analysis Reproducibility (10 points)

| Score Range | Criteria | Framework Reference |
|-------------|----------|-------------------|
| 9-10 | Documented methodology, repeatable steps, validated tools, peer review | NIST 800-86 §5, ISO 27042 |
| 7-8 | Good documentation, mostly repeatable, some gaps | - |
| 5-6 | Basic analysis notes, questionable reproducibility | - |
| 0-4 | Poor documentation, irreproducible methods | - |

**Reproducibility Elements**:
- Step-by-step analysis documentation
- Tool version and configuration records
- Parameter settings and search terms
- Output capture and retention
- Ability to replicate findings independently

---

#### Dimension 6: Tool Validation (10 points)

| Score Range | Criteria | Framework Reference |
|-------------|----------|-------------------|
| 9-10 | All tools NIST CFTT validated or equivalent, documented testing | NIST CFTT, Daubert criteria |
| 7-8 | Most tools validated, documented justifications for others | - |
| 5-6 | Some validation, incomplete documentation | - |
| 0-4 | Unvalidated tools, no documentation, admissibility risk | - |

**Validation Requirements**:
- NIST CFTT validation preferred
- Vendor documentation of testing
- Internal validation procedures
- Known error rates and limitations
- Version tracking and updates

---

#### Dimension 7: Reporting & Admissibility (10 points)

| Score Range | Criteria | Framework Reference |
|-------------|----------|-------------------|
| 9-10 | Professional report, clear findings, expert witness ready, Daubert compliant | Daubert/Frye, NIST 800-86 §6 |
| 7-8 | Good reporting, minor clarity issues, mostly admissible | - |
| 5-6 | Basic report, unclear findings, potential admissibility issues | - |
| 0-4 | Poor reporting, unclear methodology, likely inadmissible | - |

**Report Requirements**:
- Clear statement of findings
- Methodology explanation
- Tool and version documentation
- Chain of custody summary
- Limitations and caveats
- Expert qualifications
- References to standards

---

#### Dimension 8: Privacy/Legal Authority (10 points)

| Score Range | Criteria | Framework Reference |
|-------------|----------|-------------------|
| 9-10 | Clear legal authority documented, privacy considerations addressed, consent obtained | ACPO Principle 4, local laws |
| 7-8 | Good authority documentation, privacy addressed | - |
| 5-6 | Basic authority, incomplete privacy consideration | - |
| 0-4 | Unclear or no legal authority, privacy violations, illegal collection | - |

**Authority & Privacy Elements**:
- Search warrant or subpoena documentation
- Consent forms when applicable
- Data minimization principles
- Privacy impact assessment
- Compliance with GDPR, CCPA, etc.
- Handling of PII and sensitive data

---

### Weighted Total Score Calculation

- Dimensions 1-4: 15 points each (60% of total) - Core evidence handling
- Dimensions 5-6: 10 points each (20% of total) - Analysis and tooling
- Dimensions 7-8: 10 points each (20% of total) - Legal and reporting

**Score Bands**:
- **90-100**: Excellent - Framework-aligned, court-ready
- **75-89**: Good - Minor gaps, generally admissible
- **60-74**: Fair - Significant gaps, potential admissibility issues
- **0-59**: Poor - Major deficiencies, likely inadmissible

---

## 4. Key Research Papers

### Recent Publications (2024-2026)

| Title | Authors | Year | Venue | DOI/Link | Relevance |
|-------|---------|------|-------|----------|-----------|
| Ensuring the Integrity of Digital Evidence: The Role of Chain of Custody | ResearchGate | 2024 | ResearchGate | [Link](https://www.researchage.net/publication/387792852) | Chain of custody procedures and documentation requirements |
| An Empirical Assessment of Digital Forensic Process Reliability | MDPI | 2024 | Future Internet 6(2):57 | [DOI](https://www.mdpi.com/2624-800X/6/2/57) | ISO 27037 adherence in e-commerce fraud investigations |
| Digital Forensics Tool Testing Program | NIST CFTT | Ongoing | NIST.gov | [Link](https://www.nist.gov/itl/ssd/software-quality-group/computer-forensics-tool-testing-program-cftt) | Tool validation standards and testing methodologies |

### Foundational Papers

| Title | Authors | Year | Venue | DOI/Link | Relevance |
|-------|---------|------|-------|----------|-----------|
| Daubert v. Merrell Dow Pharmaceuticals | US Supreme Court | 1993 | US Supreme Court | - | Scientific evidence admissibility criteria |
| Frye v. United States | US Court of Appeals | 1923 | DC Circuit | - | General acceptance test for evidence |
| Digital Evidence Crime Scene Investigation | Various | 2000s | Academic/Industry | - | Early digital forensics methodology development |

### Ongoing Research Areas
- Cloud forensics and distributed evidence
- IoT device acquisition and analysis
- Machine learning in forensic analysis
- Blockchain and cryptocurrency forensics
- Deepfake detection and authentication
- Volatile memory acquisition advances

---

## 5. State-of-the-Art Methods & Tools

### Evidence Hierarchy (for scoring weight)

1. **Systematic Review** - Highest authority, meta-analysis of multiple studies
2. **Meta-Analysis** - Statistical combination of multiple studies
3. **RCT/Benchmark** - Controlled testing or tool benchmarks
4. **Cohort/Case Study** - Real-world application analysis
5. **Expert Opinion** - Consensus of qualified experts
6. **Blog/Industry Article** - Lowest authority, informational only

### Current Tool Categories

**Acquisition Tools**:
- FTKEY Imager (NIST CFTT validated)
- EnCase (NIST CFTT validated)
- dd/dc3dd (command-line imaging)
- Write-blockers (Tableau, CRU, etc.)
- Volatile memory acquisition (Mandiant Memoryze, WinEN)

**Analysis Tools**:
- Autopsy (open-source, NIST reviewed)
- Sleuth Kit (library underlying Autopsy)
- EnCase (commercial, validated)
- FTK (commercial, validated)
- X-Ways Forensics (commercial)

**Mobile Forensics**:
- Cellebrite (industry standard)
- Magnet AXIOM
- Oxygen Forensics
- MSAB XRY

**Cloud Forensics Tools**:
- Cloud acquisition suites
- API-based collection tools
- SaaS investigation platforms

**Integrity Verification**:
- Hash calculation tools (md5deep, sha256deep)
- File system analysis tools
- Registry analysis utilities

---

## 6. Authoritative Data Sources

### Primary Sources

1. **NIST Computer Forensics Tool Testing Program (CFTT)**
   - URL: https://www.nist.gov/itl/ssd/software-quality-group/computer-forensics-tool-testing-program-cftt
   - Focus: Tool validation and testing methodologies
   - Update frequency: Ongoing
   - Authority level: US National Standard

2. **ISO/IEC 27037:2012**
   - URL: https://www.iso.org/standard/44381.html
   - Focus: Digital evidence handling procedures
   - Update frequency: Standard revision in progress (2024)
   - Authority level: International Standard

3. **SWGDE (Scientific Working Group on Digital Evidence)**
   - URL: https://www.swgde.org
   - Focus: Consensus-based best practices
   - Update frequency: Regular updates through 2025
   - Authority level: Scientific consensus

4. **DFIR Community Resources**
   - URL: https://www.forensicfocus.com
   - Focus: Industry news, techniques, discussions
   - Update frequency: Daily
   - Authority level: Professional community

5. **ArXiv Research Repository**
   - Categories: cs.CR (Cryptography and Security)
   - URL: https://arxiv.org/list/cs.CR/recent
   - Focus: Academic research publications
   - Update frequency: Daily
   - Authority level: Peer-reviewed research

### Secondary Sources
- Digital forensics textbooks and manuals
- Industry conference proceedings (DFRWS, HTCIA)
- Government forensic laboratory guidelines
- Law enforcement training materials

---

## 7. Compliance & Legal Standards

### International Standards
- **ISO 27000 Series**: 27037, 27041, 27042, 27043, 27050
- **ISO 15481**: Information security incident investigation
- **ISO 31000**: Risk management principles

### US Standards
- **NIST SP 800-86**: Forensic techniques in incident response
- **NIST SP 800-61**: Incident handling guide
- **Daubert Standard**: Scientific evidence admissibility
- **Frye Standard**: General acceptance test (state-level)

### European Standards
- **ACPO Guidelines**: UK police practices
- **ENFSI Guidelines**: European Network of Forensic Science Institutes
- **GDPR Considerations**: Privacy and data protection
- **eIDAS**: Electronic identification and trust services

### Compliance Requirements by Domain

**Law Enforcement**:
- Criminal procedure rules
- Evidence authentication requirements
- Chain of custody standards
- Expert witness qualification

**Corporate/Private Sector**:
- Internal investigation policies
- Employment law considerations
- Data privacy regulations
- Cross-border data transfer rules

**Civil Litigation**:
- eDiscovery procedures (FRCP Rule 26)
- Evidence preservation obligations
- Spoliation prevention
- Expert report requirements

---

## 8. Quality Checkpoints

### Evidence Integrity Gates

1. **Pre-Acquisition Gate**
   - Legal authority confirmed
   - Scope defined
   - Tools validated
   - Personnel qualified

2. **Acquisition Gate**
   - Write-blocking verified
   - Hash calculation completed
   - Imaging process documented
   - Original secured

3. **Post-Acquisition Gate**
   - Hash verification successful
   - Image integrity confirmed
   - Chain of custody initiated
   - Storage secured

4. **Analysis Gate**
   - Methodology documented
   - Tools version-tracked
   - Findings reproducible
   - Limitations acknowledged

5. **Reporting Gate**
   - Findings clearly stated
   - Methodology explained
   - References cited
   - Expert qualifications included

6. **Admissibility Gate**
   - Daubert/Frye criteria met
   - Chain of custody complete
   - Tool validation documented
   - Peer review available

### Common Failure Points

| Failure Type | Impact | Prevention |
|--------------|--------|------------|
| No write-blocking | Evidence alteration, inadmissibility | Use hardware write-blockers |
| MD5-only hashing | Weak integrity claims | Use SHA-256 or better |
| Chain gaps | Admissibility challenges | Continuous documentation |
| Unvalidated tools | Daubert challenges | Use NIST CFTT validated tools |
| Poor documentation | Irreproducible analysis | Step-by-step documentation |
| No legal authority | Exclusionary rule, fruit of poisonous tree | Verify warrants/consent first |

---

## 9. Knowledge Update Log

### 2026-06-18 - Initial Knowledge Base Population
- Framework specifications fully documented
- Scoring rubrics defined with evidence-based criteria
- Research papers and sources catalogued
- Quality checkpoints established
- Tool categories and validation standards included

### Automated Crawl Batches
*Future automated entries will appear here, appended by `tools/knowledge_updater.py`*

---

## Credibility Statement

This knowledge base is maintained for the **Digital Forensics Process Support** skill and draws from:
- International standards (ISO/IEC)
- National standards (NIST)
- Scientific working groups (SWGDE)
- Peer-reviewed research
- Industry best practices

All scoring criteria and framework references are tied to citable sources. Updates are performed weekly via automated crawl and manual review of authoritative sources.

## Disclaimers

- This knowledge base is for informational purposes only
- Not a substitute for licensed legal advice
- Jurisdiction-specific requirements may vary
- Standards evolve; always verify current versions
- Professional judgment required in application

<!-- End of SECOND-KNOWLEDGE-BRAIN.md -->
