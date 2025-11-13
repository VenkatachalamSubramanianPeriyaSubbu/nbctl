# Resolve Command Examples

Practical examples for merging notebooks with conflict detection.

## Basic Usage

### 3-Way Merge

```bash
nbctl resolve base.ipynb ours.ipynb theirs.ipynb -o merged.ipynb
```

### Check Conflicts Only

```bash
nbctl resolve base.ipynb ours.ipynb theirs.ipynb --check-conflicts
```

### With Report

```bash
nbctl resolve base.ipynb ours.ipynb theirs.ipynb -o merged.ipynb --report
```

## Merge Strategies

### Auto Merge (Default)

```bash
nbctl resolve base.ipynb ours.ipynb theirs.ipynb -o merged.ipynb --strategy auto
```

### Prefer Ours

```bash
nbctl resolve base.ipynb ours.ipynb theirs.ipynb -o merged.ipynb --strategy ours
```

### Prefer Theirs

```bash
nbctl resolve base.ipynb ours.ipynb theirs.ipynb -o merged.ipynb --strategy theirs
```

### Cell Append

```bash
nbctl resolve base.ipynb ours.ipynb theirs.ipynb -o merged.ipynb --strategy cell-append
```

## Git Integration

### During Git Merge

```bash
#!/bin/bash
# When git merge creates notebook conflicts

nb="notebook.ipynb"

# Extract three versions
git show :1:$nb > base_$nb      # Common ancestor
git show :2:$nb > ours_$nb      # Your version
git show :3:$nb > theirs_$nb    # Their version

# Resolve
nbctl resolve base_$nb ours_$nb theirs_$nb -o $nb --report

# Check result
if [ $? -eq 0 ]; then
    git add $nb
    echo "Resolved $nb"
else
    echo "⚠ Manual resolution needed for $nb"
fi

# Cleanup
rm base_$nb ours_$nb theirs_$nb
```

### Automated Git Merge

After `git-setup`, this happens automatically:

```bash
# Git uses nbctl resolve automatically
git merge feature-branch

# If conflicts in notebooks, they're resolved intelligently
```

### Custom Merge Driver Script

`.git/hooks/merge-notebook`:

```bash
#!/bin/bash
# Custom merge driver for notebooks

BASE=$1
OURS=$2
THEIRS=$3

nbctl resolve "$BASE" "$OURS" "$THEIRS" -o "$OURS" --strategy auto

exit $?
```

## Workflow Examples

### Feature Branch Merge

```bash
#!/bin/bash
# Merge feature branch with conflict handling

feature_branch="feature/new-analysis"
nb="analysis.ipynb"

# Attempt merge
git merge $feature_branch

# If conflicts
if git status | grep -q "both modified.*$nb"; then
    # Get versions
    git show :1:$nb > base.ipynb
    git show :2:$nb > ours.ipynb
    git show :3:$nb > theirs.ipynb
    
    # Resolve
    nbctl resolve base.ipynb ours.ipynb theirs.ipynb -o $nb --report
    
    # Review and complete
    git add $nb
    git commit -m "Merge $feature_branch (resolved $nb)"
    
    rm base.ipynb ours.ipynb theirs.ipynb
fi
```

### Collaborative Merge

```bash
#!/bin/bash
# Merge notebooks from multiple collaborators

base="original.ipynb"
alice="alice_version.ipynb"
bob="bob_version.ipynb"

# Merge Alice's changes
nbctl resolve $base $base $alice -o step1.ipynb --strategy auto

# Merge Bob's changes
nbctl resolve $base step1.ipynb $bob -o final.ipynb --strategy auto

rm step1.ipynb
echo "Merged all contributions"
```

### Review Before Merge

```bash
#!/bin/bash
# Check for conflicts before merging

# Check conflicts
if nbctl resolve base.ipynb ours.ipynb theirs.ipynb --check-conflicts; then
    echo "No conflicts, proceeding with merge"
    nbctl resolve base.ipynb ours.ipynb theirs.ipynb -o merged.ipynb
else
    echo "Conflicts detected, review required"
    nbctl resolve base.ipynb ours.ipynb theirs.ipynb --check-conflicts
    exit 1
fi
```

## Advanced Examples

### Batch Conflict Resolution

```bash
#!/bin/bash
# Resolve multiple notebooks after merge

for nb in $(git diff --name-only --diff-filter=U | grep '\.ipynb$'); do
    echo "Resolving $nb..."
    
    git show :1:$nb > base_$nb
    git show :2:$nb > ours_$nb
    git show :3:$nb > theirs_$nb
    
    if nbctl resolve base_$nb ours_$nb theirs_$nb -o $nb; then
        git add $nb
        echo "Resolved $nb"
    else
        echo "⚠ Manual resolution needed: $nb"
    fi
    
    rm base_$nb ours_$nb theirs_$nb
done
```

### Strategy Selection

```bash
#!/bin/bash
# Intelligently select strategy

base="base.ipynb"
ours="ours.ipynb"
theirs="theirs.ipynb"
output="merged.ipynb"

# Check conflicts
if nbctl resolve $base $ours $theirs --check-conflicts; then
    # No conflicts, use auto
    nbctl resolve $base $ours $theirs -o $output --strategy auto
else
    # Has conflicts, ask user
    echo "Conflicts detected. Choose strategy:"
    echo "1) Auto (default)"
    echo "2) Prefer ours"
    echo "3) Prefer theirs"
    echo "4) Cell append"
    read -p "Choice: " choice
    
    case $choice in
        2) strategy="ours" ;;
        3) strategy="theirs" ;;
        4) strategy="cell-append" ;;
        *) strategy="auto" ;;
    esac
    
    nbctl resolve $base $ours $theirs -o $output --strategy $strategy --report
fi
```

### Post-Merge Validation

```bash
#!/bin/bash
# Merge and validate result

# Merge
nbctl resolve base.ipynb ours.ipynb theirs.ipynb -o merged.ipynb

# Validate by running
if nbctl run merged.ipynb --timeout 300; then
    echo "Merge successful and notebook runs"
    git add merged.ipynb
    git commit -m "Merge notebooks (validated)"
else
    echo "Merged notebook has errors"
    exit 1
fi
```

## CI/CD Integration

### GitHub Actions

```yaml
name: Resolve Notebook Conflicts
on: [pull_request]

jobs:
  resolve:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
        with:
          fetch-depth: 0
      
      - name: Install nbctl
        run: pip install nbctl
      
      - name: Check for notebook conflicts
        run: |
          for nb in *.ipynb; do
            git show origin/main:$nb > base_$nb 2>/dev/null || continue
            git show HEAD:$nb > ours_$nb
            
            if ! nbctl resolve base_$nb base_$nb ours_$nb --check-conflicts; then
              echo "⚠ Conflicts in $nb"
              exit 1
            fi
            
            rm base_$nb ours_$nb
          done
```

## Tips & Best Practices

### 1. Always Check First

```bash
# Check for conflicts before merging
nbctl resolve base.ipynb ours.ipynb theirs.ipynb --check-conflicts

# If clean, proceed
if [ $? -eq 0 ]; then
    nbctl resolve base.ipynb ours.ipynb theirs.ipynb -o merged.ipynb
fi
```

### 2. Use Reports

```bash
# Get detailed merge information
nbctl resolve base.ipynb ours.ipynb theirs.ipynb -o merged.ipynb --report
```

### 3. Validate After Merge

```bash
# Merge
nbctl resolve base.ipynb ours.ipynb theirs.ipynb -o merged.ipynb

# Validate
nbctl lint merged.ipynb
nbctl run merged.ipynb --timeout 300
```

### 4. Keep Conflict Markers

If conflicts remain, manually resolve:

```python
# Look for conflict markers in merged.ipynb
# <<<<<<<<< OURS
# code version 1
# =========
# code version 2
# >>>>>>>>> THEIRS
```

## Related Examples

- [Diff Examples](diff.md) - Compare versions before merging
- [Git-Setup Examples](git-setup.md) - Configure automatic resolve
- [Combine Examples](combine.md) - Simple concatenation

