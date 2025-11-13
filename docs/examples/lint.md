# Lint Command Examples

Practical examples for checking notebook code quality.

## Basic Usage

### Lint Single Notebook

```bash
nbctl lint notebook.ipynb
```

### Custom Cell Length

```bash
nbctl lint notebook.ipynb --max-cell-length 150
```

## Workflow Examples

### Pre-Commit Check

```bash
#!/bin/bash
# Check all notebooks before commit

for nb in $(git diff --cached --name-only | grep '\.ipynb$'); do
    echo "Linting $nb..."
    if ! nbctl lint "$nb"; then
        echo "Linting failed for $nb"
        echo "Fix issues and try again"
        exit 1
    fi
done

echo "All notebooks pass linting"
```

### Team Quality Check

```bash
# Check all notebooks with strict standards
for nb in *.ipynb; do
    nbctl lint "$nb" --max-cell-length 75
done
```

### Lint and Fix Workflow

```bash
#!/bin/bash
# 1. Lint to find issues
nbctl lint notebook.ipynb

# 2. Format to fix style
nbctl format notebook.ipynb

# 3. Lint again to verify
nbctl lint notebook.ipynb
```

## CI/CD Examples

### GitHub Actions

```yaml
name: Lint Notebooks
on: [pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2
      - name: Install nbutils
        run: pip install nbutils
      - name: Lint notebooks
        run: |
          for nb in *.ipynb; do
            nbctl lint "$nb" || exit 1
          done
```

### Pre-Commit Hook

`.git/hooks/pre-commit`:

```bash
#!/bin/bash
# Lint notebooks on commit

for nb in $(git diff --cached --name-only | grep '\.ipynb$'); do
    nbctl lint "$nb" --max-cell-length 100 || exit 1
done
```

## Advanced Examples

### Generate Lint Report

```bash
#!/bin/bash
# Generate HTML report of linting issues

echo "<html><body><h1>Lint Report</h1>" > lint-report.html

for nb in *.ipynb; do
    echo "<h2>$nb</h2><pre>" >> lint-report.html
    nbctl lint "$nb" >> lint-report.html 2>&1
    echo "</pre>" >> lint-report.html
done

echo "</body></html>" >> lint-report.html
```

### Enforce Standards by Project Type

```bash
# Teaching/Tutorial notebooks (strict)
nbctl lint tutorial.ipynb --max-cell-length 30

# Analysis notebooks (moderate)
nbctl lint analysis.ipynb --max-cell-length 75

# Research notebooks (lenient)
nbctl lint research.ipynb --max-cell-length 150
```

### Track Lint Issues Over Time

```bash
#!/bin/bash
# Track lint issues in CSV

date=$(date +%Y-%m-%d)
issues=$(nbctl lint notebook.ipynb | grep -c "Issue" || echo "0")
echo "$date,$issues" >> lint-history.csv
```

## Tips & Best Practices

### 1. Fix Issues Incrementally

```bash
# Lint to see all issues
nbctl lint notebook.ipynb

# Fix one type at a time:
# - Remove unused imports
# - Split long cells
# - Remove empty cells
```

### 2. Use with Format

```bash
# Format fixes style issues
nbctl format notebook.ipynb

# Lint catches structural issues
nbctl lint notebook.ipynb
```

### 3. Team Standards Document

Create `NOTEBOOK_STANDARDS.md`:

```markdown
# Notebook Standards

## Linting
All notebooks must pass:
\`\`\`bash
nbctl lint notebook.ipynb --max-cell-length 75
\`\`\`

## Before Committing
1. Run lint
2. Run format
3. Run lint again
\`\`\`
```

## Related Examples

- [Format Examples](format.md) - Auto-fix style issues
- [Clean Examples](clean.md) - Clean notebooks
- [Info Examples](info.md) - Analyze notebook structure

