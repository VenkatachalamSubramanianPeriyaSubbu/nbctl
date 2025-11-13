# Git-Setup Command Examples

Practical examples for configuring git for notebooks.

## Initial Setup

### Setup New Repository

```bash
# Initialize git
git init

# Configure for notebooks
nbctl git-setup

# Review configuration
cat .gitattributes
cat .gitignore
```

### Setup Existing Repository

```bash
# Navigate to repository
cd my-project

# Run git-setup
nbctl git-setup

# Commit configuration
git add .gitattributes .gitignore
git commit -m "Configure git for notebooks"
```

## Team Setup

### Repository Owner

```bash
# 1. Setup git
nbctl git-setup

# 2. Review files
cat .gitattributes .gitignore

# 3. Commit and push
git add .gitattributes .gitignore
git commit -m "Add notebook git configuration"
git push
```

### Team Members

```bash
# 1. Pull configuration
git pull

# 2. Enable custom drivers
nbctl git-setup

# 3. Verify
git config --list | grep nbutils
```

## Verification

### Verify Configuration

```bash
# Check .gitattributes
cat .gitattributes
# Should show: *.ipynb diff=nbctl merge=nbutils

# Check git config
git config --list | grep nbutils
# Should show diff and merge drivers

# Test diff
git diff notebook.ipynb
# Should show clean code diff, not JSON
```

### Test Diff Driver

```bash
# Make changes to notebook
# (edit in Jupyter)

# Check diff (uses nbctl automatically)
git diff notebook.ipynb

# Should show:
# - Only source code changes
# - No output changes
# - No metadata changes
```

### Test Merge Driver

```bash
# Create test branch
git checkout -b test-branch

# Make changes
# (edit notebook)

# Commit
git add notebook.ipynb
git commit -m "Test changes"

# Switch and make conflicting changes
git checkout main
# (edit same notebook differently)
git add notebook.ipynb
git commit -m "Main changes"

# Merge (uses nbctl resolve automatically)
git merge test-branch
```

## Workflow Examples

### New Project Setup

```bash
#!/bin/bash
# setup-notebook-project.sh

# Create project
mkdir my-analysis
cd my-analysis

# Initialize git
git init

# Configure for notebooks
nbctl git-setup

# Create initial notebook
# (create in Jupyter)

# First commit
git add .
git commit -m "Initial commit with notebook configuration"

echo "Project setup complete"
```

### Clean Git History Workflow

```bash
# 1. Setup git config
nbctl git-setup

# 2. Clean all existing notebooks
for nb in *.ipynb; do
    nbctl clean "$nb"
done

# 3. Commit cleaned notebooks
git add *.ipynb
git commit -m "Clean notebooks for git"

# 4. From now on, diffs will be clean
```

### Migrate Existing Project

```bash
#!/bin/bash
# migrate-to-nbutils.sh

# 1. Backup
git branch backup-before-nbutils

# 2. Setup nbutils
nbctl git-setup

# 3. Clean all notebooks
for nb in **/*.ipynb; do
    nbctl clean "$nb"
done

# 4. Commit
git add .
git commit -m "Migrate to nbctl for notebook management"

echo "Migration complete"
echo "Backup branch: backup-before-nbutils"
```

## Advanced Configuration

### Custom .gitignore Rules

After setup, add project-specific rules:

```bash
# Run git-setup first
nbctl git-setup

# Add custom rules
cat >> .gitignore << EOF

# Project-specific
data/*.csv
models/*.pkl
secrets.env
*.log
EOF

git add .gitignore
git commit -m "Add project-specific gitignore rules"
```

### Multiple Notebook Types

```bash
# Setup for different notebook types
nbctl git-setup

# Add to .gitattributes
cat >> .gitattributes << EOF
*.ipynb diff=nbctl merge=nbutils
notebooks/*.ipynb diff=nbctl merge=nbutils
experiments/*.ipynb diff=nbctl merge=nbutils
EOF
```

## Troubleshooting Examples

### Reset Configuration

```bash
# If configuration is broken
rm .gitattributes .gitignore

# Run setup again
nbctl git-setup

# Verify
git config --list | grep nbutils
```

### Fix Diff Not Working

```bash
# Re-run setup
nbctl git-setup

# Force git to reread attributes
git rm --cached -r .
git reset --hard

# Test
git diff notebook.ipynb
```

### Per-Repository vs Global

```bash
# Current setup is per-repository
git config --local --list | grep nbutils

# To make global (not recommended)
# git config --global diff.nbutils.command 'nbctl diff'
```

## CI/CD Integration

### Verify Setup in CI

```yaml
name: Verify Git Setup
on: [push]

jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install nbutils
        run: pip install nbutils
      - name: Setup git
        run: nbctl git-setup
      - name: Verify configuration
        run: |
          test -f .gitattributes || exit 1
          test -f .gitignore || exit 1
          git config --list | grep nbctl || exit 1
```

## Tips & Best Practices

### 1. Run Once Per Repository

```bash
# Only need to run once
nbctl git-setup

# Team members also run it
# (to enable custom drivers locally)
```

### 2. Commit Configuration Files

```bash
# Always commit these
git add .gitattributes .gitignore
git commit -m "Configure git for notebooks"
```

### 3. Document for Team

Create `SETUP.md`:

```markdown
# Project Setup

## For New Team Members

After cloning the repository:

\`\`\`bash
pip install nbutils
nbctl git-setup
\`\`\`

This enables intelligent notebook diffs and merges.
\`\`\`
```

### 4. Test Configuration

```bash
# After setup, test with a notebook change
echo 'print("test")' >> test.ipynb
git diff test.ipynb
# Should show clean diff
```

## Related Examples

- [Clean Examples](clean.md) - Clean notebooks for git
- [Diff Examples](diff.md) - Compare notebooks
- [Resolve Examples](resolve.md) - Merge notebooks

