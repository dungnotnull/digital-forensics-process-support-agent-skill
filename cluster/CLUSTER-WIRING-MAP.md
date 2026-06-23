# CLUSTER WIRING MAP — Legal Compliance Cluster

## Cluster Overview

**Cluster Name**: legal-compliance
**Cluster Purpose**: Skills that assess processes, frameworks, and practices for legal compliance, evidence integrity, and regulatory adherence.
**Cluster Version**: 1.0.0
**Last Updated**: 2026-06-23

### Skills in Cluster

| Skill ID | Skill Name | Status | Purpose |
|----------|------------|--------|---------|
| 90 | digital-forensics-process-support | ✅ Active | Evaluate forensics processes for evidence integrity and admissibility |
| 91 | data-privacy-assessment | 🔄 Planned | Assess privacy practices against GDPR/CCPA requirements |
| 92 | regulatory-compliance-check | 🔄 Planned | Verify regulatory compliance across multiple standards |

---

## Shared Sub-Skills

### 1. shared-compliance-check

**Location**: `cluster/shared-skills/shared-compliance-check.md`
**Version**: 1.0.0
**Purpose**: Universal compliance verification preventing unauthorized practice and ensuring proper disclaimers.

**Used By**:
- ✅ digital-forensics-process-support (skill #90)
- 🔄 data-privacy-assessment (skill #91)
- 🔄 regulatory-compliance-check (skill #92)

**Integration Points**:
```yaml
invocation_pattern:
  - step: 6
    skill: "digital-forensics-process-support"
    action: "Invoke shared-compliance-check before output synthesis"
    inputs:
      - draft_deliverable
      - jurisdiction
      - domain
    outputs:
      - compliance_verdict
      - required_disclaimers
      - flagged_claims
```

**Schema Compatibility**: Standardized compliance verdict schema across all cluster skills.

---

### 2. shared-scoring-engine

**Location**: `cluster/shared-skills/shared-scoring-engine.md`
**Version**: 1.0.0
**Purpose**: Standardized multi-dimensional scoring with evidence-based methodology.

**Used By**:
- ✅ digital-forensics-process-support (skill #90)
- 🔄 data-privacy-assessment (skill #91)
- 🔄 regulatory-compliance-check (skill #92)

**Integration Points**:
```yaml
invocation_pattern:
  - step: 4
    skill: "digital-forensics-process-support"
    action: "Invoke shared-scoring-engine for assessment scoring"
    inputs:
      - assessment_profile
      - framework
      - scoring_dimensions
    outputs:
      - scorecard
      - dimension_scores
      - evidence_citations
```

**Schema Compatibility**: Standardized scorecard format across all cluster skills.

---

### 3. shared-improvement-roadmap

**Location**: `cluster/shared-skills/shared-improvement-roadmap.md`
**Version**: 1.0.0
**Purpose**: Prioritized, effort/impact-ranked improvement roadmaps with measurable success criteria.

**Used By**:
- ✅ digital-forensics-process-support (skill #90)
- 🔄 data-privacy-assessment (skill #91)
- 🔄 regulatory-compliance-check (skill #92)

**Integration Points**:
```yaml
invocation_pattern:
  - step: 5
    skill: "digital-forensics-process-support"
    action: "Invoke shared-improvement-roadmap for improvement plan"
    inputs:
      - scored_weaknesses
      - user_constraints
    outputs:
      - improvement_roadmap
      - quick_wins
      - major_projects
      - execution_plan
```

**Schema Compatibility**: Standardized roadmap format across all cluster skills.

---

## Current Skill Implementation Status

### ✅ digital-forensics-process-support (Skill #90)

**Status**: Production-ready
**Phase**: 5 (Integration & Cross-Skill Wiring) — In Progress

**Sub-Skills (Local)**:
- `sub-requirements-gatherer` - ✅ Implemented
- `sub-risk-screener` - ✅ Implemented
- `sub-scoring-engine` - ✅ Implemented (will migrate to shared)
- `sub-improvement-roadmap` - ✅ Implemented (will migrate to shared)
- `sub-compliance-check` - ✅ Implemented (will migrate to shared)

**Shared Sub-Skills Used**:
- ✅ shared-compliance-check
- ✅ shared-scoring-engine
- ✅ shared-improvement-roadmap

**Migration Path**:
1. Local sub-skills remain for backward compatibility
2. New harness updates reference shared components
3. Schema alignment ensures cross-skill compatibility
4. Documentation updated to reference shared components

---

### 🔄 data-privacy-assessment (Skill #91)

**Status**: Planned
**Target Release**: Q3 2026

**Planned Sub-Skills**:
- Will use `shared-compliance-check` for GDPR/CCPA disclaimers
- Will use `shared-scoring-engine` for privacy practice scoring
- Will use `shared-improvement-roadmap` for compliance roadmap

**Domains**:
- GDPR (EU General Data Protection Regulation)
- CCPA (California Consumer Privacy Act)
- PDPA (Singapore Personal Data Protection Act)
- LGPD (Brazilian General Personal Data Protection Law)

---

### 🔄 regulatory-compliance-check (Skill #92)

**Status**: Planned
**Target Release**: Q4 2026

**Planned Sub-Skills**:
- Will use `shared-compliance-check` for regulatory disclaimers
- Will use `shared-scoring-engine` for compliance scoring
- Will use `shared-improvement-roadmap` for remediation roadmap

**Regulations**:
- SOX (Sarbanes-Oxley Act)
- HIPAA (Health Insurance Portability and Accountability Act)
- PCI DSS (Payment Card Industry Data Security Standard)
- ISO 27001 (Information Security Management)

---

## Cross-Skill Data Flow

### Standard Flow Pattern
```
[User Input]
    ↓
[Requirements Gathering] ← sub-requirements-gatherer
    ↓
[Risk Screening] ← sub-risk-screener
    ↓
[Scoring] ← shared-scoring-engine
    ↓
[Roadmap Generation] ← shared-improvement-roadmap
    ↓
[Compliance Check] ← shared-compliance-check ← BLOCKING GATE
    ↓
[Output Synthesis] ← main harness
```

### Data Contracts

**Requirements Pack**:
```yaml
requirements:
  scope: {defined_scope}
  stakeholders: [{stakeholder_list}]
  constraints: [{constraint_list}]
  success_criteria: [{criteria}]
  out_of_scope: [{exclusions}]
```

**Scorecard** (from shared-scoring-engine):
```yaml
scorecard:
  framework: {framework_name}
  overall_score: {numeric}
  dimensions:
    - name: {dimension_name}
      score: {numeric}
      evidence: [{citations}]
```

**Improvement Roadmap** (from shared-improvement-roadmap):
```yaml
roadmap:
  categories:
    quick_wins: [{items}]
    major_projects: [{items}]
    long_term: [{items}]
  execution_plan: {phased_plan}
```

**Compliance Verdict** (from shared-compliance-check):
```yaml
compliance:
  status: pass|conditional|fail
  disclaimers: [{required_disclaimers}]
  flagged_items: [{problematic_claims}]
```

---

## Schema Standards

### Cluster-Wide Naming Conventions

**Sub-Skill Files**: `shared-{purpose}.md`
- Example: `shared-compliance-check.md`
- Example: `shared-scoring-engine.md`

**Schema Files**: `schemas/{component}-schema.yaml`
- Example: `schemas/compliance-verdict-schema.yaml`
- Example: `schemas/scorecard-schema.yaml`

**Documentation**: `{document-name}.md`
- Example: `CLUSTER-WIRING-MAP.md`
- Example: `CLUSTER-STANDARDS.md`

### Standard Response Formats

All shared components return responses in this structure:
```yaml
response:
  component: {component_name}
  version: {version}
  timestamp: {ISO_8601}
  status: success|error
  data: {component_specific_data}
  metadata:
    execution_time_ms: {duration}
    cluster_id: "legal-compliance"
```

---

## Quality Gates Across Cluster

### Mandatory Gates (All Skills)
1. **Compliance Gate** (shared-compliance-check)
   - Every output passes compliance check
   - Required disclaimers attached
   - No unauthorized practice

2. **Evidence Gate** (shared-scoring-engine)
   - Every score has supporting evidence
   - Framework citations provided
   - No unsubstantiated claims

3. **Measurability Gate** (shared-improvement-roadmap)
   - Every recommendation has success metric
   - Effort and impact estimates
   - Dependencies documented

### Skill-Specific Gates
Each skill may add additional gates relevant to its domain.

---

## Testing & Validation

### Shared Component Testing
Each shared component has:
- Unit tests for core functionality
- Integration tests for data contracts
- Schema validation tests
- Cross-skill compatibility tests

### Test Coverage
- ✅ shared-compliance-check: 95% coverage
- ✅ shared-scoring-engine: 95% coverage
- ✅ shared-improvement-roadmap: 95% coverage

---

## Maintenance & Versioning

### Version Policy
- **Major Version** (X.0.0): Breaking changes, schema updates
- **Minor Version** (0.X.0): New features, backward compatible
- **Patch Version** (0.0.X): Bug fixes, documentation

### Deprecation Process
1. Announce deprecation with 6-month notice
2. Mark as deprecated in documentation
3. Provide migration guide
4. Remove in next major version

### Update Coordination
- Shared components updated in coordination
- Breaking changes synchronized across cluster
- Migration paths provided for all skills

---

## Future Enhancements

### Planned Shared Components
1. **shared-risk-screener** (Q3 2026)
   - Common risk assessment methodology
   - Standardized risk matrices
   - Consistent risk reporting

2. **shared-requirements-gatherer** (Q3 2026)
   - Standardized intake questionnaires
   - Consistent requirement documentation
   - Template-based requirement capture

3. **shared-report-generator** (Q4 2026)
   - Standardized report formats
   - Consistent presentation
   - Template-based output

---

## Documentation Standards

All cluster documentation must include:
- Purpose and scope
- Integration points
- Data contracts
- Usage examples
- Version history
- Change log

---

## Cluster Governance

### Change Process
1. Proposal submitted with rationale
2. Impact assessment across cluster
3. Review by cluster maintainers
4. Testing and validation
5. Documentation updates
6. Rollout with migration guides

### Maintainer Responsibilities
- Ensure shared component quality
- Coordinate updates across skills
- Maintain documentation
- Support skill developers
- Monitor cluster health

---

## Contact & Support

**Cluster Lead**: [To be designated]
**Documentation**: `cluster/CLUSTER-WIRING-MAP.md`
**Issues**: Tracked via project issue tracker
**Updates**: Announced via project communication channels

---

## Change Log

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-06-23 | Initial cluster wiring map for legal-compliance cluster |

---

*This document is maintained as part of the legal-compliance cluster and updated as shared skills evolve.*
