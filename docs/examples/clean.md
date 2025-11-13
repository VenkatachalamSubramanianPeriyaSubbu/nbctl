# Clean Command Examples

Practical examples for using `nbctl clean` to prepare notebooks for version control.

## Basic Usage

### Clean Notebook In-Place

Remove outputs and metadata from a notebook:

```bash linenums="1"
nbctl clean analysis.ipynb
```

Result: Notebook cleaned, outputs removed, ready for git.

---

### Preview Changes (Dry Run)

See what would be changed without modifying the file:

```bash linenums="1"
nbctl clean analysis.ipynb --dry-run
```

Output:
```
Dry run - no changes made
Would clean: analysis.ipynb
- Outputs removed: 15 cells
- Execution counts reset: 20 cells
- Metadata cleaned: 1 notebook
```

---

### Save to Different File

Clean and save to a new file:

```bash linenums="1"
nbctl clean original.ipynb -o cleaned.ipynb
```

Result: `original.ipynb` unchanged, `cleaned.ipynb` created.

---

## Selective Cleaning

### Keep Outputs

Clean metadata but preserve cell outputs:

```bash linenums="1"
nbctl clean notebook.ipynb --keep-outputs
```

Use case: When outputs are important but metadata is not.

---

### Keep Execution Counts

Clean outputs but preserve execution order:

```bash linenums="1"
nbctl clean notebook.ipynb --keep-execution-count
```

Use case: When execution order matters for understanding.

---

### Keep Metadata

Clean only outputs, preserve everything else:

```bash linenums="1"
nbctl clean notebook.ipynb --keep-metadata
```

---

## Workflow Examples

### Pre-Commit Workflow

Clean notebook before every commit:

```bash linenums="1"
# 1. Make changes to notebook
# 2. Clean before committing
nbctl clean analysis.ipynb

# 3. Verify changes
git diff analysis.ipynb

# 4. Commit
git add analysis.ipynb
git commit -m "Update analysis"
```

---

### Batch Cleaning

Clean all notebooks in a directory:

```bash linenums="1"
# Method 1: Loop
for nb in *.ipynb; do
    nbctl clean "$nb"
done

# Method 2: With backup
for nb in *.ipynb; do
    cp "$nb" "$nb.backup"
    nbctl clean "$nb"
done
```

---

### Clean Before Code Review

Clean and create a review copy:

```bash linenums="1"
nbctl clean analysis.ipynb -o analysis_review.ipynb
```

Share `analysis_review.ipynb` for review (no clutter).

---

## Git Integration

### Pre-Commit Hook

Create `.git/hooks/pre-commit`:

```bash linenums="1"
#!/bin/bash
# Clean all notebooks before commit

for nb in $(git diff --cached --name-only --diff-filter=ACM | grep '\.ipynb$'); do
    nbctl clean "$nb"
    git add "$nb"
done
```

Make it executable:
```bash linenums="1"
chmod +x .git/hooks/pre-commit
```

---

### Clean Changed Notebooks Only

Clean only notebooks that changed:

```bash linenums="1"
git diff --name-only | grep '\.ipynb$' | while read nb; do
    nbctl clean "$nb"
done
```

---

## Advanced Examples

### Clean with Verification

Clean and verify the notebook still works:

```bash linenums="1"
# 1. Clean
nbctl clean notebook.ipynb

# 2. Run to regenerate outputs
nbctl run notebook.ipynb

# 3. Check for errors
if [ $? -eq 0 ]; then
    echo "Notebook cleaned and verified"
else
    echo "Notebook has errors"
fi
```

---

### Clean and Format

Clean and format in one workflow:

```bash linenums="1"
nbctl clean notebook.ipynb
nbctl format notebook.ipynb
git add notebook.ipynb
git commit -m "Clean and format notebook"
```

---

## Team Workflows

### Team Standard

Establish team cleaning standard:

```bash linenums="1"
# teams/clean-standard.sh
#!/bin/bash
# Team standard: clean before commit

for nb in "$@"; do
    echo "Cleaning $nb..."
    nbctl clean "$nb" --keep-metadata
done

echo "All notebooks cleaned"
```

Usage:
```bash linenums="1"
./teams/clean-standard.sh *.ipynb
```

---

### Code Review Preparation

Prepare notebooks for review:

```bash linenums="1"
# 1. Clean all notebooks
for nb in *.ipynb; do
    nbctl clean "$nb" -o "review/$nb"
done

# 2. Create review package
tar -czf review-package.tar.gz review/

# 3. Share review-package.tar.gz
```

---

## CI/CD Examples

### GitHub Actions

`.github/workflows/clean-notebooks.yml`:

```yaml linenums="1"
name: Clean Notebooks
on: [push, pull_request]

jobs:
  clean:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      
      - name: Install nbutils
        run: pip install nbutils
      
      - name: Clean notebooks
        run: |
          for nb in *.ipynb; do
            nbctl clean "$nb"
          done
      
      - name: Check for changes
        run: |
          if git diff --quiet; then
            echo "All notebooks already clean"
          else
            echo "Some notebooks need cleaning"
            git diff --name-only
            exit 1
          fi
```

---

## Error Handling

### Handle Missing Files

```bash linenums="1"
if [ -f notebook.ipynb ]; then
    nbctl clean notebook.ipynb
else
    echo "Error: notebook.ipynb not found"
    exit 1
fi
```

---

### Handle Cleaning Failures

```bash linenums="1"
if nbctl clean notebook.ipynb; then
    echo "Cleaned successfully"
    git add notebook.ipynb
else
    echo "Cleaning failed"
    exit 1
fi
```

---

## Tips and Best Practices

### Always Test First

```bash linenums="1"
# Test with dry run
nbctl clean notebook.ipynb --dry-run

# If OK, clean for real
nbctl clean notebook.ipynb
```

### Keep Backups

```bash linenums="1"
# Create backup before cleaning
cp notebook.ipynb notebook.ipynb.backup
nbctl clean notebook.ipynb
```

### Clean Regularly

```bash linenums="1"
# Daily cleaning
for nb in *.ipynb; do
    nbctl clean "$nb"
done
git add *.ipynb
git commit -m "Daily notebook cleanup"
```

---

## Related Examples

[Git Setup Examples](git-setup.md) - Configure automatic cleaning
[Diff Examples](diff.md) - Compare cleaned notebooks
[Format Examples](format.md) - Format after cleaning

---

## Next Steps

Learn about [git integration](../cli/git-setup.md)
Explore [diff command](../cli/diff.md)
Check [format command](../cli/format.md)
