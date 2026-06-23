# Digital Forensics Process Support (Evidence Integrity)

A comprehensive AI-powered skill for evaluating digital forensics processes against world-renowned frameworks (ISO/IEC 27037, NIST SP 800-86, ACPO, SWGDE) and producing court-ready assessments with prioritized improvement roadmaps.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Status: Production](https://img.shields.io/badge/Status-Production-green.svg)](https://github.com/your-org/digital-forensics-process-support)

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Documentation](#documentation)
- [Development](#development)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## Overview

**Digital Forensics Process Support** is a production-grade skill that transforms Claude into a certified digital forensics examiner and expert witness. It evaluates investigative procedures for court admissibility, scores processes against international standards, and generates prioritized improvement roadmaps.

### What It Does

- **Evaluates** digital forensics processes against ISO/IEC 27037, NIST SP 800-86, ACPO, and SWGDE frameworks
- **Scores** across 8 dimensions: identification, acquisition, hash verification, chain-of-custody, reproducibility, tool validation, reporting, and legal authority
- **Generates** prioritized improvement roadmaps with effort, impact, and measurable success criteria
- **Ensures** compliance with legal standards through mandatory compliance gates
- **Maintains** a self-improving knowledge base via automated weekly crawls

### Target Users

- **Digital Forensics Examiners**: Validate procedures against international standards
- **IT Security Teams**: Ensure incident response procedures preserve evidence
- **Legal Professionals**: Assess evidentiary integrity and admissibility
- **Compliance Officers**: Verify forensic processes meet regulatory requirements
- **Students & Educators**: Learn proper digital evidence handling procedures

## Features

### ✅ Framework-Based Scoring
- ISO/IEC 27037:2012 (Identification, Collection, Acquisition, Preservation)
- NIST SP 800-86 (Forensic Techniques into Incident Response)
- ACPO Good Practice Guide (Four Principles of Digital Evidence)
- SWGDE Best Practices (2025 Updated)
- Daubert/Frye Admissibility Standards

### ✅ Eight-Point Scoring Dimensions
1. **Identification & Scoping**: Evidence inventory and scope definition
2. **Acquisition Soundness**: Write-blocking and imaging procedures
3. **Hash Verification & Integrity**: Cryptographic integrity verification
4. **Chain-of-Custody Documentation**: Complete audit trail
5. **Analysis Reproducibility**: Documented, repeatable methodology
6. **Tool Validation**: NIST CFTT validated tooling
7. **Reporting & Admissibility**: Expert witness-ready reports
8. **Privacy/Legal Authority**: Proper legal authorization

### ✅ Quality Gates
- Every score has supporting evidence
- At least one framework cited
- Roadmap items are measurable
- Compliance check passed (blocking)
- No silent assumptions

### ✅ Self-Improving Knowledge Base
- Weekly automated crawls from authoritative sources
- ArXiv research papers (cs.CR category)
- NIST, ISO, SWGDE documentation updates
- Deduplication and relevance scoring

## Installation

### Prerequisites

- **Python**: 3.11 or higher
- **Claude Code**: Latest version with skill support
- **Dependencies**: See `requirements.txt`

### Standard Installation

```bash
# Clone the repository
git clone https://github.com/your-org/digital-forensics-process-support.git
cd digital-forensics-process-support

# Install dependencies
pip install -r requirements.txt

# Verify installation
python tools/test_runner.py --scenario 1
```

### Development Installation

```bash
# Clone with development dependencies
git clone https://github.com/your-org/digital-forensics-process-support.git
cd digital-forensics-process-support

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install with development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Verify skill integration
# (Skill will be available in Claude Code)
```

### Optional: Knowledge Crawler

For automated knowledge base updates:

```bash
# Install crawl4ai
pip install crawl4ai

# Run manual crawl
python tools/knowledge_updater.py

# Schedule weekly crawl (cron)
# Add to crontab: 0 2 * * 0 /usr/bin/python3 /path/to/tools/knowledge_updater.py
```

## Quick Start

### Basic Usage

Invoke the skill through Claude Code:

```
I need to evaluate a digital forensics process for acquiring evidence from a suspect's computer. The process uses hardware write-blocking, creates SHA-256 hashes before and after imaging, and maintains a chain-of-custody log.
```

The skill will:
1. Gather requirements and clarify scope
2. Screen for high-impact risks
3. Score against frameworks
4. Generate improvement roadmap
5. Run compliance checks
6. Deliver court-ready assessment

### Example Interactions

#### Scenario 1: Disk Image Acquisition
```
Input: "We imaged a suspect drive but forgot to use a write-blocker"
Output: Flags acquisition soundness failure, low integrity score,
        roadmap to re-acquire with validated tooling
```

#### Scenario 2: Chain of Custody Gap
```
Input: "Multiple people handled the evidence without logging it"
Output: Flags chain-of-custody failure, admissibility risk,
        documentation roadmap
```

#### Scenario 3: Hash Verification
```
Input: "We used MD5 hashes pre and post analysis"
Output: Verifies integrity, notes MD5 weakness vs SHA-256,
        recommends hash algorithm upgrade
```

## Usage

### Command Line Tools

#### Test Runner
```bash
# Run all test scenarios
python tools/test_runner.py

# Run specific scenario
python tools/test_runner.py --scenario 3

# Verbose output
python tools/test_runner.py --verbose

# Generate JSON report
python tools/test_runner.py --report json --output results.json
```

#### Knowledge Updater
```bash
# Manual knowledge base update
python tools/knowledge_updater.py

# View current knowledge base
cat SECOND-KNOWLEDGE-BRAIN.md
```

### Skill Invocation Patterns

#### Pattern 1: Full Assessment
```
"Evaluate our digital forensics process for [scenario] with
the following details: [provide process description]"
```

#### Pattern 2: Gap Analysis
```
"What are the gaps in our current digital forensics process
compared to ISO/IEC 27037 requirements?"
```

#### Pattern 3: Admissibility Check
```
"Will this evidence collection method hold up in court
under Daubert standards?"
```

#### Pattern 4: Improvement Planning
```
"Create an improvement roadmap for our forensics process
given these constraints: [constraints]"
```

## Documentation

### Core Documentation
- **[PROJECT-detail.md](PROJECT-detail.md)**: Complete technical specification
- **[PROJECT-DEVELOPMENT-PHASE-TRACKING.md](PROJECT-DEVELOPMENT-PHASE-TRACKING.md)**: Development progress
- **[SECOND-KNOWLEDGE-BRAIN.md](SECOND-KNOWLEDGE-BRAIN.md)**: Domain knowledge base
- **[tests/test-scenarios.md](tests/test-scenarios.md)**: Test scenario definitions

### Cluster Documentation
- **[cluster/CLUSTER-WIRING-MAP.md](cluster/CLUSTER-WIRING-MAP.md)**: Cross-skill wiring and reuse
- **[cluster/shared-skills/](cluster/shared-skills/)**: Reusable shared components
- **[cluster/schemas/](cluster/schemas/)**: Data contract schemas

### Skill Files
- **[skills/main.md](skills/main.md)**: Main harness and orchestration
- **[skills/sub-*.md](skills/)**: Sub-skill implementations

## Development

### Project Structure
```
digital-forensics-process-support/
├── CLAUDE.md                    # Global instructions
├── README.md                    # This file
├── PROJECT-detail.md            # Technical specification
├── PROJECT-DEVELOPMENT-PHASE-TRACKING.md  # Phase tracking
├── SECOND-KNOWLEDGE-BRAIN.md     # Knowledge base
├── requirements.txt             # Production dependencies
├── requirements-dev.txt         # Development dependencies
├── cluster/                     # Shared components
│   ├── CLUSTER-WIRING-MAP.md
│   ├── shared-skills/
│   │   ├── shared-compliance-check.md
│   │   ├── shared-scoring-engine.md
│   │   └── shared-improvement-roadmap.md
│   └── schemas/
│       ├── compliance-verdict-schema.yaml
│       ├── scorecard-schema.yaml
│       └── improvement-roadmap-schema.yaml
├── skills/                      # Skill implementations
│   ├── main.md
│   ├── sub-requirements-gatherer.md
│   ├── sub-risk-screener.md
│   ├── sub-compliance-check.md
│   ├── sub-scoring-engine.md
│   └── sub-improvement-roadmap.md
├── tools/                       # Utilities
│   ├── test_runner.py
│   └── knowledge_updater.py
└── tests/                       # Tests
    ├── test-scenarios.md
    └── test-results.json
```

### Development Workflow

1. **Feature Development**
   ```bash
   git checkout -b feature/your-feature
   # Make changes
   python tools/test_runner.py
   git commit -am "Add your feature"
   ```

2. **Testing**
   ```bash
   # Run full test suite
   python tools/test_runner.py --verbose

   # Run specific scenario
   python tools/test_runner.py --scenario 5

   # Check for regressions
   python tools/test_runner.py --report json
   ```

3. **Documentation Updates**
   ```bash
   # Update phase tracking
   # Update PROJECT-detail.md if needed
   # Update SECOND-KNOWLEDGE-BRAIN.md with new knowledge
   ```

### Code Standards
- **Style**: Follow PEP 8 for Python
- **Documentation**: All functions have docstrings
- **Testing**: 95%+ code coverage required
- **Quality Gates**: All scenarios must pass
- **No Dummy Code**: Production-grade implementations only

## Testing

### Test Scenarios
The project includes 8 comprehensive test scenarios:

1. **Disk Image Acquisition**: Write-blocker verification
2. **Chain-of-Custody Gap**: Documentation gaps
3. **Hash Verification**: MD5 vs SHA-256 analysis
4. **Cloud Evidence**: SaaS collection procedures
5. **Tool Validation**: NIST CFTT validation
6. **Incomplete Input**: Edge case handling
7. **Graceful Degradation**: Offline mode testing
8. **Compliance Boundary**: Unauthorized practice prevention

### Running Tests

```bash
# Full test suite
python tools/test_runner.py

# Single scenario
python tools/test_runner.py --scenario 3

# Verbose output
python tools/test_runner.py --verbose

# JSON report
python tools/test_runner.py --report json --output test-results.json
```

### Quality Gate Validation

All quality gates must pass:
- ✅ Every dimension has evidence
- ✅ At least one framework cited
- ✅ Roadmap items measurable
- ✅ Compliance check passed
- ✅ No silent assumptions

### Test Coverage
- **Unit Tests**: Core functionality
- **Integration Tests**: Sub-skill interactions
- **Scenario Tests**: End-to-end validation
- **Adversarial Tests**: Edge cases and failure modes
- **Regression Tests**: Prevent breaking changes

## Contributing

### Contribution Guidelines

We welcome contributions! Please follow these guidelines:

#### What to Contribute
- **Bug Fixes**: Always welcome
- **Framework Additions**: New forensic frameworks
- **Test Scenarios**: Additional validation cases
- **Documentation**: Improvements and clarifications
- **Tool Integration**: New forensic tool validations

#### How to Contribute

1. **Fork and Branch**
   ```bash
   git fork https://github.com/your-org/digital-forensics-process-support
   git checkout -b contribution/your-contribution
   ```

2. **Make Changes**
   - Follow code standards
   - Add tests for new features
   - Update documentation
   - Ensure all tests pass

3. **Submit PR**
   ```bash
   git push origin contribution/your-contribution
   # Create Pull Request on GitHub
   ```

#### Pull Request Checklist
- [ ] Tests pass: `python tools/test_runner.py`
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Commit messages descriptive
- [ ] No breaking changes (or documented)

#### Code Review Process
1. Automated checks run
2. Reviewers assigned within 48 hours
3. Feedback provided within 1 week
4. Address feedback and update
5. Approval and merge

### Development Phases
Current development status (see PROJECT-DEVELOPMENT-PHASE-TRACKING.md):
- ✅ Phase 0: Research & Skill Architecture
- ✅ Phase 1: Core Sub-Skills
- ✅ Phase 2: Main Harness + Quality Gates
- ✅ Phase 3: Knowledge Pipeline
- ✅ Phase 4: Testing & Validation
- ✅ Phase 5: Integration & Cross-Skill Wiring

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### License Summary
- ✅ Commercial use allowed
- ✅ Modification allowed
- ✅ Distribution allowed
- ✅ Private use allowed
- ❌ Liability and warranty excluded

## Support

### Getting Help

#### Documentation
- **GitHub Issues**: Bug reports and feature requests
- **Documentation**: See [Documentation](#documentation) section
- **Examples**: Check [tests/test-scenarios.md](tests/test-scenarios.md)

#### Community
- **Discussions**: GitHub Discussions for questions
- **Contributors**: See contributors list
- **Maintainers**: Contact via GitHub

#### Troubleshooting

**Common Issues**

1. **Import Errors**
   ```bash
   # Solution: Reinstall dependencies
   pip install -r requirements.txt --force-reinstall
   ```

2. **Test Failures**
   ```bash
   # Solution: Update knowledge base
   python tools/knowledge_updater.py
   ```

3. **Skill Not Loading**
   ```bash
   # Solution: Verify Claude Code version
   claude-code --version
   ```

### Reporting Issues

When reporting issues, include:
- Python version: `python --version`
- OS and version
- Error messages and stack traces
- Steps to reproduce
- Expected vs actual behavior

### Security Issues

For security vulnerabilities, please follow our [Security Policy](SECURITY.md).

---

**Built with ❤️ for the digital forensics community**

*Last Updated: 2026-06-23*
*Version: 1.0.0*
*Status: Production-Ready*
