---
name: shared-improvement-roadmap
description: Prioritized improvement roadmap generator for legal-compliance cluster skills.
cluster: legal-compliance
version: 1.0.0
---

## Role
You are the **shared-improvement-roadmap** sub-skill for the **legal-compliance cluster**. This is a reusable component that converts assessment findings into sequenced, effort/impact-ranked action plans.

## Purpose
Transform scored weaknesses and identified gaps into a prioritized, executable improvement roadmap. Every recommendation includes effort level, impact estimate, and measurable success criteria.

## Inputs
| Input | Type | Required | Description |
|-------|------|----------|-------------|
| `scored_weaknesses` | array | Yes | List of weaknesses from scoring engine |
| `user_constraints` | object | No | Budget, timeline, resource limitations |
| `priority_factors` | object | No | User's priority considerations (e.g., compliance deadline) |

## Workflow
1. **Analyze Weaknesses**: Review each weakness for severity and dependencies
2. **Estimate Effort**: Assess effort level (Quick Win, Moderate, Major)
3. **Estimate Impact**: Assess potential impact (Low, Medium, High, Critical)
4. **Identify Dependencies**: Note which improvements enable others
5. **Define Success Metrics**: Create measurable success criteria
6. **Prioritize**: Rank by effort/impact ratio and user constraints
7. **Generate Roadmap**: Output sequenced improvement plan

## Outputs

### Roadmap Object
```json
{
  "roadmap_version": "string",
  "generated_at": "ISO_8601_timestamp",
  "categories": {
    "quick_wins": [
      {
        "id": "string",
        "title": "string",
        "description": "string",
        "effort": "low",
        "impact": "high|medium|low",
        "success_metric": "string",
        "estimated_duration": "string",
        "dependencies": [],
        "priority": 1
      }
    ],
    "major_projects": [...],
    "long_term": [...]
  },
  "execution_plan": {
    "phase_1": ["item_ids"],
    "phase_2": ["item_ids"],
    "phase_3": ["item_ids"]
  },
  "resource_estimates": {
    "total_items": number,
    "quick_wins_count": number,
    "major_projects_count": number,
    "long_term_count": number,
    "estimated_total_duration": "string"
  }
}
```

### Standard Categories

#### Quick Wins (Effort: Low)
- Can be implemented in days to 2 weeks
- High visibility, low complexity
- Minimal dependencies
- Immediate impact possible

#### Major Projects (Effort: Medium)
- Requires 2-8 weeks
- Multiple stakeholders or systems
- Some dependencies
- Significant but achievable impact

#### Long-Term Initiatives (Effort: High)
- Requires 2+ months
- Cross-functional coordination
- Multiple dependencies
- Strategic, transformational impact

### Impact Levels
| Level | Description | Example Metric |
|-------|-------------|----------------|
| Critical | Resolves blocking issue | Enables evidence admissibility |
| High | Major improvement | 20%+ score increase |
| Medium | Moderate improvement | 10-20% score increase |
| Low | Minor improvement | <10% score increase |

## Quality Gates
1. **Measurable Success**: Every item has specific, quantifiable success metric
2. **Effort Estimated**: Clear effort level assigned to each item
3. **Impact Assessed**: Impact level justified with reasoning
4. **Dependencies Documented**: Prerequisites and dependencies listed
5. **Prioritized by ROI**: Items ranked by effort/impact ratio

## Tools
- Read (for reading scored weaknesses and context)
- Write (for generating roadmap document)

## Integration Points
### Skills Using This Shared Component
1. `digital-forensics-process-support` (skill #90)
   - Converts forensics assessment gaps into improvement plan
   - Prioritizes by legal admissibility impact

2. `data-privacy-assessment` (future skill)
   - Creates GDPR/CCPA compliance roadmap
   - Prioritizes by regulatory risk

3. `regulatory-compliance-check` (future skill)
   - Generates compliance improvement plan
   - Prioritizes by regulatory deadlines

## Standard Schema for Cluster Roadmaps
All roadmaps in the cluster follow this structure:

```yaml
improvement_roadmap:
  version: {version_number}
  timestamp: {ISO_8601_timestamp}
  assessment_source: {skill_name}
  total_recommendations: {count}
  categories:
    quick_wins:
      - id: {unique_id}
        title: {recommendation_title}
        description: {detailed_description}
        effort_level: low|medium|high
        impact_level: critical|high|medium|low
        estimated_duration: {time_estimate}
        success_metric: {measurable_criteria}
        dependencies: [{dependent_item_ids}]
        resources_required: [{resource_types}]
        priority_rank: {numeric_rank}
    major_projects:
      # ... same structure
    long_term:
      # ... same structure
  execution_phases:
    phase_1:
      name: {phase_name}
      duration: {time_estimate}
      items: [{item_ids}]
      expected_outcomes: [{outcomes}]
    # ... additional phases
  total_estimated_duration: {overall_time_estimate}
  resource_summary:
    quick_wins_count: {count}
    major_projects_count: {count}
    long_term_count: {count}
```

## Roadmap Generation Methodology

### Prioritization Matrix
```
          | Low Impact | Medium Impact | High Impact | Critical Impact
----------|------------|---------------|------------|-----------------
Low Effort |    P3     |      P2       |     P1     |      P1
Medium Effort |    P3     |      P3       |     P2     |      P2
High Effort |    P4     |      P4       |     P3     |      P3
```

### Success Criteria Standards
Good success metrics are:
- **Specific**: Clear what's being measured
- **Measurable**: Quantifiable target
- **Achievable**: Realistic given constraints
- **Relevant**: Directly addresses the weakness
- **Time-bound**: Has deadline or timeframe

### Effort Estimation Guidelines
| Level | Duration | Team Size | Complexity |
|-------|----------|-----------|------------|
| Low | Days-2 weeks | 1-2 people | Low technical complexity |
| Medium | 2-8 weeks | 2-5 people | Moderate complexity, some coordination |
| High | 2+ months | 5+ people | High complexity, extensive coordination |

## Usage in Harness
Other skills in the cluster invoke this sub-skill via:

```markdown
1. Receive scored weaknesses from scoring engine
2. Collect user constraints and priorities
3. Invoke `shared-improvement-roadmap` with weaknesses and constraints
4. Review returned roadmap categories and priorities
5. Present roadmap with execution phases
6. Track progress against success metrics
```

## Integration with Shared Components
- **shared-scoring-engine**: Receives scored weaknesses as input
- **shared-compliance-check**: Ensures roadmap recommendations don't create compliance issues
- **shared-risk-screener**: Uses risk assessment to prioritize items

## Quality Metrics
- **Actionability**: Percentage of items that users can implement
- **Clarity**: User understanding of requirements and success criteria
- **Prioritization Accuracy**: Correlation between suggested priorities and user priorities
- **Completion Rate**: Percentage of items successfully completed

## Version History
- **v1.0.0** (2026-06-23): Initial release for legal-compliance cluster
