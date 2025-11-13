# Format Command Examples

Practical examples for auto-formatting notebooks with black.

## Basic Usage

### Format Notebook

```bash
nbctl format notebook.ipynb
```

### Custom Line Length

```bash
nbctl format notebook.ipynb --line-length 100
```

### Save to Different Location

```bash
nbctl format notebook.ipynb --output-dir ./formatted/
```

## Workflow Examples

### Pre-Commit Formatting

```bash
#!/bin/bash
# Format all notebooks before commit

for nb in $(git diff --cached --name-only | grep '\.ipynb$'); do
    echo "Formatting $nb..."
    nbctl format "$nb"
    git add "$nb"
done

echo "All notebooks formatted"
```

### Batch Formatting

```bash
# Format all notebooks in project
for nb in **/*.ipynb; do
    nbctl format "$nb"
done
```

### Format and Review

```bash
# 1. Format
nbctl format notebook.ipynb

# 2. Review changes
git diff notebook.ipynb

# 3. If OK, commit
git add notebook.ipynb
git commit -m "Format notebook with black"
```

## Team Standards

### Enforce Team Style

```bash
#!/bin/bash
# teams/format-all.sh

# Format with team line length
for nb in *.ipynb; do
    nbctl format "$nb" --line-length 88
done
```

### Check Formatting in CI

```yaml
name: Check Formatting
on: [pull_request]

jobs:
  format-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2
      - name: Install nbctl
        run: pip install nbctl
      - name: Check formatting
        run: |
          for nb in *.ipynb; do
            nbctl format "$nb" --output-dir temp/
            if ! diff "$nb" "temp/$nb"; then
              echo "$nb needs formatting"
              exit 1
            fi
          done
```

## Advanced Examples

### Format with Backup

```bash
#!/bin/bash
# Format with automatic backup

nb="$1"
backup="${nb}.backup"

# Create backup
cp "$nb" "$backup"

# Format
if nbctl format "$nb"; then
    echo "Formatted successfully"
    rm "$backup"
else
    echo "Formatting failed, restoring backup"
    mv "$backup" "$nb"
    exit 1
fi
```

### Conditional Formatting

```bash
# Format only if changed recently
if [ "notebook.ipynb" -nt "notebook.ipynb.formatted" ]; then
    nbctl format notebook.ipynb
    touch notebook.ipynb.formatted
fi
```

### Format and Lint Pipeline

```bash
#!/bin/bash
# Complete quality pipeline

nb="$1"

echo "Formatting $nb..."
nbctl format "$nb"

echo "Linting $nb..."
nbctl lint "$nb"

echo "Cleaning $nb..."
nbctl clean "$nb"

echo "Quality pipeline complete"
```

## CI/CD Integration

### Pre-Commit Hook

`.git/hooks/pre-commit`:

```bash
#!/bin/bash
# Auto-format notebooks on commit

for nb in $(git diff --cached --name-only | grep '\.ipynb$'); do
    nbctl format "$nb" --line-length 88
    git add "$nb"
done
```

### GitHub Actions Auto-Format

```yaml
name: Auto-Format
on: [push]

jobs:
  format:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Format notebooks
        run: |
          pip install nbctl
          for nb in *.ipynb; do
            nbctl format "$nb"
          done
      - name: Commit changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add *.ipynb
          git diff --quiet || git commit -m "Auto-format notebooks"
          git push
```

## Tips & Best Practices

### 1. Format Regularly

```bash
# Weekly formatting
for nb in *.ipynb; do
    nbctl format "$nb"
done
git commit -am "Weekly formatting"
```

### 2. Check Before Formatting

```bash
# Preview what would change
nbctl format notebook.ipynb --output-dir temp/
diff notebook.ipynb temp/notebook.ipynb
```

### 3. Team Consistency

```bash
# Use same line length across team
# Add to .gitattributes or document
echo "Line length: 88" > .formatting-config
nbctl format *.ipynb --line-length 88
```

## Related Examples

- [Lint Examples](lint.md) - Check code quality
- [Clean Examples](clean.md) - Clean notebooks
- [Git-Setup Examples](git-setup.md) - Configure git

