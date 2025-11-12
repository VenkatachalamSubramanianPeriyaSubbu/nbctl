# Welcome to nbutils

Welcome to nbutils - The Swiss Army Knife for Jupyter Notebooks.

## What is nbutils?

nbutils is a command-line toolkit that solves common problems when working with Jupyter notebooks. Whether you're a student learning Python, a researcher conducting analysis, or a data scientist building models, nbutils makes your workflow smoother.

## The Problem

Jupyter notebooks are great for learning and experimentation, but they have challenges:

**Version Control Issues**
Notebooks store outputs and metadata, making git diffs huge and merge conflicts painful.

**Code Quality**
No built-in linting or formatting means inconsistent code across notebooks.

**Security Risks**
Easy to accidentally commit API keys or passwords.

**Manual Workflows**
Converting formats, extracting outputs, and running notebooks requires manual work.

**Production Gap**
Moving from notebook experiments to production code is time-consuming.

## The Solution

nbutils provides 13 commands that address these challenges:

**clean** - Strip outputs for clean git commits
**diff** - Compare notebooks intelligently
**resolve** - Merge notebooks with conflict detection
**info** - Analyze notebook structure
**lint** - Check code quality
**format** - Auto-format code with black
**security** - Scan for vulnerabilities
**run** - Execute notebooks from command line
**export** - Convert to HTML, PDF, Python, etc.
**extract** - Save images and data outputs
**ml-split** - Create production pipelines
**combine** - Merge multiple notebooks
**git-setup** - Configure git integration

## Who is nbutils for?

**Students**
Learn Python and data science without worrying about messy git commits. Keep your coursework organized.

**Data Analysts**
Generate reports, extract visualizations, and maintain clean analysis notebooks.

**Researchers**
Ensure reproducibility, collaborate effectively, and publish findings with confidence.

**Educators**
Create teaching materials, manage assignments, and maintain consistent code quality.

**Business Intelligence Professionals**
Automate report generation and maintain professional notebook standards.

**Data Scientists**
Move from prototype to production faster with automated pipeline generation.

## Quick Example

Here's a typical workflow with nbutils:

```bash
# Work on your notebook in Jupyter
# Run cells, create visualizations, analyze data

# Before committing:
nbutils clean notebook.ipynb    # Remove outputs
nbutils format notebook.ipynb   # Format code
nbutils lint notebook.ipynb     # Check quality

# Commit to git
git add notebook.ipynb
git commit -m "Add analysis"
```

## Key Benefits

**Cleaner Version Control**
Remove outputs before committing. Diffs show only code changes.

**Better Collaboration**
Intelligent merging reduces conflicts. Team members can work on same notebooks.

**Higher Quality**
Automated linting and formatting maintain consistent standards.

**Improved Security**
Scan for hardcoded secrets before they reach version control.

**Faster Workflows**
Automate repetitive tasks like format conversion and output extraction.

**Code Conversion**
Convert notebooks to Python code automatically.

## Getting Started

Ready to get started? Follow these steps:

1. **[Install nbutils](installation.md)** - Get up and running in minutes
2. **[Explore commands](../cli/clean.md)** - See what nbutils can do
3. **[Try examples](../examples/clean.md)** - Hands-on learning

## Need Help?

Check the [Help Guide](help.md) for:

- Command-line help
- Troubleshooting
- Bug reports
- Feature requests
- Contributing guidelines

## Simple First Steps

Try these commands to see nbutils in action:

```bash
# Get notebook information
nbutils info your-notebook.ipynb

# Clean a notebook
nbutils clean your-notebook.ipynb --dry-run

# Check for security issues
nbutils security your-notebook.ipynb
```

---

**Let's make working with Jupyter notebooks easier and more professional.**
