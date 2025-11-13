# Diff Command Examples

Practical examples for comparing notebooks intelligently.

## Basic Usage

### Compare Two Notebooks

```bash
nbctl diff old.ipynb new.ipynb
```

### Unified Format

```bash
nbctl diff old.ipynb new.ipynb --format unified
```

### JSON Format

```bash
nbctl diff old.ipynb new.ipynb --format json
```

### Code Only

```bash
nbctl diff old.ipynb new.ipynb --code-only
```

### Statistics Only

```bash
nbctl diff old.ipynb new.ipynb --stats
```

## Workflow Examples

### Code Review Workflow

```bash
#!/bin/bash
# Review changes before merging

# Get notebooks from branches
git show feature:notebook.ipynb > feature_notebook.ipynb
git show main:notebook.ipynb > main_notebook.ipynb

# Compare
nbctl diff main_notebook.ipynb feature_notebook.ipynb

# If OK, merge
git merge feature
```

### Pre-Merge Check

```bash
# Before merging, see what changed
git show origin/main:notebook.ipynb > main.ipynb
nbctl diff main.ipynb notebook.ipynb --stats

# If significant changes, review carefully
if [ $? -ne 0 ]; then
    nbctl diff main.ipynb notebook.ipynb
fi
```

### Track Changes Over Time

```bash
#!/bin/bash
# Compare with previous versions

# Last commit
git show HEAD~1:notebook.ipynb > prev.ipynb
nbctl diff prev.ipynb notebook.ipynb

# Last week
git show HEAD@{1.week.ago}:notebook.ipynb > last_week.ipynb
nbctl diff last_week.ipynb notebook.ipynb
```

## Advanced Examples

### Generate Diff Report

```bash
#!/bin/bash
# Generate HTML diff report

echo "<html><body><h1>Notebook Changes</h1>" > diff-report.html

for nb in *.ipynb; do
    git show HEAD~1:"$nb" > prev_"$nb" 2>/dev/null || continue
    echo "<h2>$nb</h2><pre>" >> diff-report.html
    nbctl diff prev_"$nb" "$nb" >> diff-report.html 2>&1
    echo "</pre>" >> diff-report.html
    rm prev_"$nb"
done

echo "</body></html>" >> diff-report.html
```

### Compare with Production

```bash
# Compare local with production version
scp prod:/path/notebook.ipynb prod_notebook.ipynb
nbctl diff prod_notebook.ipynb notebook.ipynb --code-only
```

### Batch Comparison

```bash
#!/bin/bash
# Compare all notebooks in two directories

for nb in dir1/*.ipynb; do
    name=$(basename "$nb")
    if [ -f "dir2/$name" ]; then
        echo "=== $name ==="
        nbctl diff "$nb" "dir2/$name" --stats
        echo
    fi
done
```

## Git Integration

### As Git Diff Tool

```bash
# After git-setup, use in git diff
git diff notebook.ipynb
# Automatically uses nbctl diff

# Or explicitly
git diff --no-ext-diff notebook.ipynb  # Standard JSON diff
git diff notebook.ipynb                # Clean nbctl diff
```

### Compare Branches

```bash
#!/bin/bash
# Compare notebook across branches

branch1="main"
branch2="feature"
nb="analysis.ipynb"

git show $branch1:$nb > ${branch1}_$nb
git show $branch2:$nb > ${branch2}_$nb

nbctl diff ${branch1}_$nb ${branch2}_$nb

rm ${branch1}_$nb ${branch2}_$nb
```

### Review Pull Request

```bash
#!/bin/bash
# Review notebooks in PR

# Fetch PR
git fetch origin pull/123/head:pr-123
git checkout pr-123

# Compare with main
for nb in *.ipynb; do
    git show main:$nb > main_$nb 2>/dev/null || continue
    echo "=== Changes in $nb ==="
    nbctl diff main_$nb $nb --code-only
    rm main_$nb
done
```

## CI/CD Examples

### Check for Large Changes

```yaml
name: Check Notebook Changes
on: [pull_request]

jobs:
  check-changes:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
        with:
          fetch-depth: 2
      - name: Install nbctl
        run: pip install nbctl
      - name: Check changes
        run: |
          for nb in *.ipynb; do
            git show HEAD^:$nb > prev_$nb 2>/dev/null || continue
            changes=$(nbctl diff prev_$nb $nb --stats | grep "Modified" | awk '{print $2}')
            if [ "$changes" -gt 10 ]; then
              echo "⚠ Large changes in $nb: $changes cells modified"
            fi
          done
```

## Automation Examples

### Daily Change Report

```bash
#!/bin/bash
# Generate daily change report

date=$(date +%Y-%m-%d)
report="changes-$date.txt"

echo "Notebook Changes - $date" > "$report"
echo "=========================" >> "$report"

for nb in *.ipynb; do
    git show HEAD~1:$nb > prev_$nb 2>/dev/null || continue
    echo -e "\n$nb:" >> "$report"
    nbctl diff prev_$nb $nb --stats >> "$report"
    rm prev_$nb
done

echo "Report saved: $report"
```

### Track Cell Count Changes

```bash
#!/bin/bash
# Track how cell counts change

nb="analysis.ipynb"
git show HEAD~1:$nb > prev.ipynb 2>/dev/null || exit

prev_cells=$(nbctl info prev.ipynb | grep "Total cells" | awk '{print $3}')
curr_cells=$(nbctl info $nb | grep "Total cells" | awk '{print $3}')
diff=$((curr_cells - prev_cells))

echo "$nb: $prev_cells → $curr_cells (${diff:+$diff})"
rm prev.ipynb
```

## Tips & Best Practices

### 1. Use Stats for Quick Overview

```bash
# Quick check
nbctl diff old.ipynb new.ipynb --stats

# If significant, detailed diff
if [ $? -eq 0 ]; then
    nbctl diff old.ipynb new.ipynb
fi
```

### 2. Use Code-Only for Technical Review

```bash
# Focus on code changes
nbctl diff old.ipynb new.ipynb --code-only
```

### 3. Use JSON for Automation

```bash
# Parse changes programmatically
nbctl diff old.ipynb new.ipynb --format json > diff.json
python process_diff.py diff.json
```

## Related Examples

- [Git-Setup Examples](git-setup.md) - Configure git diff
- [Resolve Examples](resolve.md) - Merge notebooks
- [Clean Examples](clean.md) - Clean before comparing

