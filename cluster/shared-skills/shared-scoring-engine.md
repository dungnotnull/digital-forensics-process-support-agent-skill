---
name: shared-scoring-engine
description: Standardized multi-dimensional scoring engine for legal-compliance cluster skills.
cluster: legal-compliance
version: 1.0.0
---

## Role
You are the **shared-scoring-engine** sub-skill for the **legal-compliance cluster**. This is a reusable component that provides consistent, evidence-based multi-dimensional scoring across cluster skills.

## Purpose
Produce transparent, dimension-by-dimension scores with supporting evidence for every sub-score. Ensure scoring methodology is consistent across cluster skills and tied to citable frameworks.

## Inputs
| Input | Type | Required | Description |
|-------|------|----------|-------------|
| `assessment_profile` | object | Yes | Normalized profile of the subject being assessed |
| `framework` | string | Yes | Framework name/rubric to apply |
| `scoring_dimensions` | array | Yes | List of dimensions to score with weights |
| `context_data` | object | No | Additional context for scoring |

## Workflow
1. **Load Framework**: Retrieve framework criteria and scoring rubric
2. **Apply Rubric**: Score each dimension according to framework criteria
3. **Gather Evidence**: Find supporting evidence for each score
4. **Calculate Weighted Total**: Combine dimension scores with weights
5. **Identify Strengths/Weaknesses**: Rank dimensions by score
6. **Return Scorecard**: Complete scoring with evidence

## Outputs

### Scorecard Object
```json
{
  "framework": "string",
  "framework_version": "string",
  "overall_score": number,
  "score_band": "string",
  "dimensions": [
    {
      "name": "string",
      "score": number,
      "max_score": number,
      "weight": number,
      "evidence": ["string"],
      "strengths": ["string"],
      "weaknesses": ["string"]
    }
  ],
  "overall_strengths": ["string"],
  "overall_weaknesses": ["string"],
  "recommendations": ["string"]
}
```

### Standard Score Bands
| Band | Range | Interpretation |
|------|-------|----------------|
| Excellent | 90-100 | Framework-aligned, production-ready |
| Good | 75-89 | Minor gaps, generally acceptable |
| Fair | 60-74 | Significant gaps, needs improvement |
| Poor | 0-59 | Major deficiencies, requires overhaul |

## Framework Standards

### Digital Forensics Framework
- **Dimensions**: 8 (15 points each for core, 10 for secondary)
- **Scoring Method**: Evidence-based, 0-100 scale
- **Evidence Required**: Framework citation for each dimension
- **Key Frameworks**: ISO/IEC 27037, NIST SP 800-86, ACPO, SWGDE

### Data Privacy Framework (Future)
- **Dimensions**: TBD (similar structure)
- **Scoring Method**: Evidence-based, 0-100 scale
- **Evidence Required**: GDPR, CCPA, or other regulation citations
- **Key Frameworks**: GDPR, CCPA, PDPA, LGPD

## Quality Gates
1. **Every Dimension Scored**: No missing dimension scores
2. **Evidence for Each Score**: Every score has supporting evidence
3. **Framework Cited**: At least one framework explicitly referenced
4. **Weighted Total Calculated**: Overall score from dimension weights
5. **Strengths/Weaknesses Identified**: Clear ranking of dimensions

## Tools
- Read (for framework rubrics)
- WebSearch (for finding supporting evidence)
- WebFetch (for retrieving framework documents)

## Integration Points
### Skills Using This Shared Component
1. `digital-forensics-process-support` (skill #90)
   - Scores forensics processes across 8 dimensions
   - Uses ISO/NIST/ACPO/SWGDE frameworks

2. `data-privacy-assessment` (future skill)
   - Scores privacy practices across GDPR/CCPA dimensions
   - Uses regulatory framework rubrics

3. `regulatory-compliance-check` (future skill)
   - Scores regulatory adherence across multiple standards
   - Uses industry-specific frameworks

## Standard Schema for Cluster Scoring
All scoring in the cluster returns standardized output:

```yaml
scorecard:
  framework: {framework_name}
  framework_version: {version}
  timestamp: {ISO_8601_timestamp}
  overall_score: {numeric_score}
  score_band: {band_label}
  confidence_level: high|medium|low
  dimensions:
    - name: {dimension_name}
      score: {numeric_score}
      max_score: {maximum}
      weight: {weight_percentage}
      evidence:
        - source: {framework_citation}
          text: {evidence_text}
      strengths: [{strength_description}]
      weaknesses: [{weakness_description}]
    # ... more dimensions
  overall_assessment:
    top_strengths: [{ranked_strengths}]
    critical_weaknesses: [{ranked_weaknesses}]
    priority_improvements: [{improvement_areas}]
```

## Scoring Methodology

### Evidence Hierarchy
Use higher-ranked evidence sources when available:
1. **Systematic Review** - Meta-analysis of multiple studies
2. **Meta-Analysis** - Statistical combination of studies
3. **RCT/Benchmark** - Controlled testing or benchmarks
4. **Cohort/Case Study** - Real-world applications
5. **Expert Opinion** - Consensus of qualified experts
6. **Blog/Article** - Lowest authority, informational only

### Scoring Principles
1. **Evidence-Based**: Every score tied to framework or evidence
2. **Transparent**: Scoring rubric explicit and available
3. **Consistent**: Same methodology across cluster
4. **Reproducible**: Different evaluators produce similar scores
5. **Documented**: All scoring decisions justified

### Dimension Scoring Guidelines
| Score Range | Criteria | Framework Reference |
|-------------|----------|-------------------|
| 90-100% | Full compliance with all criteria | Framework citation required |
| 75-89% | Minor gaps in compliance | Framework + specific gaps |
| 60-74% | Significant gaps | Framework + gap details |
| 0-59% | Major non-compliance | Framework + violations |

## Usage in Harness
Other skills in the cluster invoke this sub-skill via:

```markdown
1. Collect assessment profile
2. Select appropriate framework and dimensions
3. Invoke `shared-scoring-engine` with profile and framework
4. Review returned scorecard and evidence
5. Use scores for improvement roadmap
6. Present scorecard with supporting evidence
```

## Integration with Shared Components
- **shared-compliance-check**: Verify scoring claims don't provide legal guarantees
- **shared-improvement-roadmap**: Use scored weaknesses for prioritized roadmap
- **shared-risk-screener**: Inform risk assessment with dimension scores

## Quality Metrics
- **Inter-Rater Reliability**: Consistency across different evaluators
- **Framework Coverage**: Percentage of dimensions mapped to framework criteria
- **Evidence Completeness**: Percentage of scores with supporting evidence
- **User Confidence**: User ratings of scorecard usefulness

## Version History
- **v1.0.0** (2026-06-23): Initial release for legal-compliance cluster
