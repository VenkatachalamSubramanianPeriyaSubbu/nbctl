# nbctl

**The Swiss Army Knife for Jupyter Notebooks**

A comprehensive CLI toolkit for Jupyter notebooks that solves common pain points in version control, collaboration, code quality, security, and workflow automation.

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)]()
[![License](https://img.shields.io/badge/license-MIT-blue)]()
[![PyPI](https://img.shields.io/pypi/v/nbctl)](https://pypi.org/project/nbctl/)

---

## Links

- **PyPI:** https://pypi.org/project/nbctl/
- **Documentation:** https://venkatachalamsubramanianperiyasubbu.github.io/nbutils/
- **GitHub:** https://github.com/VenkatachalamSubramanianPeriyaSubbu/nbctl

---

## Quick Start

```bash
# Install nbctl
pip install nbctl

# Clean notebooks for git
nbctl clean notebook.ipynb

# Get notebook insights
nbctl info notebook.ipynb

# Scan for security issues
nbctl security notebook.ipynb
```

---

## Features

**Version Control & Collaboration**

- **clean** - Remove outputs and metadata for git
- **diff** - Compare notebooks intelligently
- **resolve** - 3-way merge with conflict detection
- **git-setup** - Configure git for notebooks

**Analysis & Quality**

- **info** - Analyze notebook statistics and dependencies
- **lint** - Check code quality and best practices
- **format** - Auto-format with black
- **security** - Find security vulnerabilities

**Workflow Automation**

- **run** - Execute notebooks from command line
- **export** - Convert to HTML, PDF, Markdown, Python
- **extract** - Extract outputs (images, graphs, data)
- **combine** - Concatenate notebooks

**Production**

- **ml-split** - Transform ML notebooks into production Python pipelines

---

## Who Uses nbctl?

nbctl is designed for anyone working with Jupyter notebooks:

- **Students**: Learning Python and data science, managing coursework notebooks
- **Data Analysts**: Creating reports, analyzing data, sharing insights
- **Researchers & Academicians**: Conducting reproducible research, publishing findings
- **Educators**: Creating teaching materials, grading assignments
- **Business Intelligence Professionals**: Building dashboards, generating automated reports
- **Data Scientists**: Developing models, transitioning notebooks to production

---

## Common Problems Solved

**Problem: Massive git diffs**
Notebooks include outputs and metadata, creating huge diffs that obscure actual code changes.

Solution: `nbctl clean` removes outputs before committing, reducing diff size by 90-95%.

**Problem: Merge conflicts**
Two people edit the same notebook, creating complex JSON conflicts.

Solution: `nbctl resolve` intelligently merges notebooks with automatic conflict detection.

**Problem: Security risks**
Easy to accidentally commit API keys, passwords, or sensitive data.

Solution: `nbctl security` scans for hardcoded secrets and vulnerabilities.

**Problem: Notebook to production**
Converting notebooks to production code is manual and time-consuming.

Solution: `nbctl ml-split` automatically generates production Python pipelines.

---

## Documentation Structure

- **[Getting Started](getting-started/welcome.md)** - Learn about nbctl, installation, and basic concepts
- **[CLI Documentation](cli/clean.md)** - Complete reference for all commands with descriptions and options
- **[Examples](examples/clean.md)** - Practical examples and use cases for every command
- **[About](about.md)** - Information about the author and how to contribute

---

## Installation

```bash
pip install nbctl
```

For detailed installation instructions, see the [Installation Guide](getting-started/installation.md).

---

## Simple Example

Here's how nbctl helps with a common workflow:

```bash
# Step 1: Work on your notebook in Jupyter
# (make changes, run cells, generate outputs)

# Step 2: Before committing to git
nbctl clean analysis.ipynb  # Remove outputs
nbctl format analysis.ipynb  # Format code
nbctl lint analysis.ipynb    # Check quality
nbctl security analysis.ipynb  # Scan for secrets

# Step 3: Commit with confidence
git add analysis.ipynb
git commit -m "Add data analysis"
```

---

## Support

- **Documentation**: You're reading it
- **Issues**: [GitHub Issues](https://github.com/VenkatachalamSubramanianPeriyaSubbu/nbctl/issues)
- **Email**: venkatachalam.sps@gmail.com

---

## License

MIT License - see [LICENSE](https://github.com/VenkatachalamSubramanianPeriyaSubbu/nbctl/blob/main/LICENSE) file for details.
