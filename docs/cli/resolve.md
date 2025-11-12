# nbutils resolve

Intelligent 3-way merge with conflict detection (powered by nbdime).

## Description

The `resolve` command performs intelligent 3-way merging of Jupyter notebooks using nbdime. It's designed for resolving git merge conflicts and combining branches with proper conflict detection and resolution.

Use this command to:
- Resolve git merge conflicts in notebooks
- Merge branches with notebook changes
- Intelligently combine conflicting notebooks
- Automate notebook merging in git workflows
- Detect and handle merge conflicts

## Usage

```bash
nbutils resolve BASE OURS THEIRS --output OUTPUT [OPTIONS]
```

## Arguments

| Argument | Description | Required |
|----------|-------------|----------|
| `BASE` | Common ancestor notebook (before changes) | Yes |
| `OURS` | Your version (local changes) | Yes |
| `THEIRS` | Other version (remote/branch changes) | Yes |

## Options

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `--output` | `-o` | PATH | Required* | Output file for merged notebook |
| `--strategy` | | TEXT | `auto` | Merge strategy: `auto`, `ours`, `theirs`, `cell-append` |
| `--check-conflicts` | | Flag | False | Check for conflicts only (no merge) |
| `--report` | | Flag | False | Show detailed merge report |

*Required unless `--check-conflicts` is used.

## 3-Way Merge Concept

Three-way merge uses three versions:

```
        BASE (common ancestor)
         /  \
        /    \
    OURS    THEIRS
    (local)  (remote)
        \    /
         \  /
       MERGED
```

**Example:**
```
BASE:    print("hello")
OURS:    print("Hello World")      # Changed capitalization
THEIRS:  print("hello world")      # Added "world"
MERGED:  print("Hello World")      # Combines both changes
```

## Merge Strategies

### 1. Auto (Default)

Intelligent automatic merging:
- Merges non-conflicting changes from both sides
- Detects real conflicts
- Adds conflict markers for manual resolution

```bash
nbutils resolve base.ipynb ours.ipynb theirs.ipynb -o merged.ipynb
```

**Use case:** Standard merge resolution, git integration

---

### 2. Ours

Prefer changes from "ours" (local version):
- Takes your version when conflicts occur
- Accepts non-conflicting changes from theirs

```bash
nbutils resolve base.ipynb ours.ipynb theirs.ipynb -o merged.ipynb --strategy ours
```

**Use case:** You know your changes should win

---

### 3. Theirs

Prefer changes from "theirs" (remote version):
- Takes their version when conflicts occur
- Accepts non-conflicting changes from ours

```bash
nbutils resolve base.ipynb ours.ipynb theirs.ipynb -o merged.ipynb --strategy theirs
```

**Use case:** Accept remote changes, your changes less important

---

### 4. Cell-Append

Append conflicting cells instead of choosing:
- Non-conflicting: merged normally
- Conflicting cells: both versions included

```bash
nbutils resolve base.ipynb ours.ipynb theirs.ipynb -o merged.ipynb --strategy cell-append
```

**Use case:** Want to see both versions, manual review later

## Conflict Detection

### Check Conflicts Only

Check if conflicts exist without creating merged file:

```bash
nbutils resolve base.ipynb ours.ipynb theirs.ipynb --check-conflicts
```

Output:
```
Checking for conflicts...

Conflicts detected: Yes

Conflicting cells:
  - Cell 5: Both modified differently
  - Cell 12: Modified in ours, deleted in theirs
  - Cell 18: Both added at same position

Summary:
  - Total conflicts: 3
  - Conflicting cells: 3
  - Auto-mergeable changes: 15
```

## Output

### Successful Merge (No Conflicts)

```
Merge completed successfully

Input:
  BASE:   base.ipynb (20 cells)
  OURS:   ours.ipynb (22 cells)
  THEIRS: theirs.ipynb (21 cells)

Result:
  Merged: merged.ipynb (23 cells)

Changes:
  - From OURS: 2 cells added, 3 cells modified
  - From THEIRS: 1 cell added, 2 cells modified
  - Conflicts: 0

All changes merged successfully!
```

---

### Merge with Conflicts

```
⚠ Merge completed with conflicts

Input:
  BASE:   base.ipynb
  OURS:   ours.ipynb
  THEIRS: theirs.ipynb

Result:
  Merged: merged.ipynb (with conflict markers)

Conflicts:
  Cell 5: Modified in both (different changes)
  Cell 12: Modified in ours, deleted in theirs

Action Required:
  Open merged.ipynb and resolve conflicts manually
  Look for cells marked with:
    <<<<<<<<< OURS
    =========
    >>>>>>>>> THEIRS
```

---

### Conflict Markers in Output

Conflicting cells are marked:

```python
# <<<<<<<<< OURS
import pandas as pd
df = pd.read_csv('data.csv')
# =========
import pandas as pd
df = pd.read_csv('new_data.csv')
# >>>>>>>>> THEIRS
```

**Resolution:** Edit the cell to keep desired version or combine.

## Detailed Report

Use `--report` for comprehensive merge information:

```bash
nbutils resolve base.ipynb ours.ipynb theirs.ipynb -o merged.ipynb --report
```

Output:
```
Detailed Merge Report

Input Notebooks:
  BASE:   base.ipynb
    - Cells: 20 (15 code, 5 markdown)
    - Size: 45.2 KB

  OURS:   ours.ipynb
    - Cells: 22 (17 code, 5 markdown)
    - Size: 52.1 KB
    - Changes from base: +2 cells, 3 modified

  THEIRS: theirs.ipynb
    - Cells: 21 (16 code, 5 markdown)
    - Size: 48.3 KB
    - Changes from base: +1 cell, 2 modified

Merge Strategy: auto

Cell-by-Cell Analysis:
  Cell 1-4: Unchanged (from base)
  Cell 5: Merged (non-conflicting changes)
  Cell 6: Added from OURS
  Cell 7: Modified in THEIRS
  Cell 8: CONFLICT (manual resolution needed)
  ...

Conflicts: 1
  Cell 8: Both modified differently

Output:
  merged.ipynb
    - Cells: 23 (18 code, 5 markdown)
    - Size: 55.7 KB
```

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success, clean merge (no conflicts) |
| 1 | Success, but conflicts present (manual resolution needed) |
| 2 | Files not found or invalid notebooks |
| 3 | Merge failed due to error |

## Git Integration

### During Git Merge Conflict

When git merge creates conflicts in notebooks:

```bash
# 1. Extract three versions
git show :1:notebook.ipynb > base.ipynb      # Common ancestor
git show :2:notebook.ipynb > ours.ipynb      # Your version
git show :3:notebook.ipynb > theirs.ipynb    # Their version

# 2. Resolve with nbutils
nbutils resolve base.ipynb ours.ipynb theirs.ipynb -o notebook.ipynb

# 3. If conflicts, manually resolve in notebook.ipynb

# 4. Mark as resolved
git add notebook.ipynb
git commit
```

---

### Automatic Git Integration

With `git-setup`, resolve is used automatically:

```bash
# 1. Set up git (once per repo)
nbutils git-setup

# 2. During merge, git uses nbutils automatically
git merge feature-branch
# If conflicts in notebooks, nbutils resolve runs automatically!
```

## Use Cases

### Merge Feature Branch

```bash
# Get three versions
git merge feature-branch  # Creates conflict
git show :1:notebook.ipynb > base.ipynb
git show :2:notebook.ipynb > ours.ipynb
git show :3:notebook.ipynb > theirs.ipynb

# Resolve
nbutils resolve base.ipynb ours.ipynb theirs.ipynb -o notebook.ipynb --report
```

---

### Accept All Remote Changes

```bash
nbutils resolve base.ipynb ours.ipynb theirs.ipynb -o merged.ipynb --strategy theirs
```

---

### Keep Your Changes

```bash
nbutils resolve base.ipynb ours.ipynb theirs.ipynb -o merged.ipynb --strategy ours
```

---

### Review Before Merging

```bash
# Check if conflicts exist
nbutils resolve base.ipynb ours.ipynb theirs.ipynb --check-conflicts

# If no conflicts, proceed with merge
nbutils resolve base.ipynb ours.ipynb theirs.ipynb -o merged.ipynb
```

## Comparison with combine

| Command | Purpose | Conflict Detection | Requires BASE | Use Case |
|---------|---------|-------------------|---------------|----------|
| **resolve** | 3-way merge | Yes | Yes | Git conflicts, branching |
| **combine** | Concatenate | No | No | Sequential joining |

## Notes

- **Powered by nbdime:** Uses production-grade nbdime merging
- **Intelligent:** Understands notebook structure
- **Cell-aware:** Merges at cell level, not line level
- **Conflict markers:** Clear markers for manual resolution
- **Git compatible:** Works seamlessly with git workflows
- **Preserves structure:** Maintains notebook integrity

## Best Practices

### 1. Check First

```bash
# Always check for conflicts first
nbutils resolve base.ipynb ours.ipynb theirs.ipynb --check-conflicts
```

### 2. Use Reports

```bash
# Get detailed information
nbutils resolve base.ipynb ours.ipynb theirs.ipynb -o merged.ipynb --report
```

### 3. Compare After

```bash
# Verify merge result
nbutils diff base.ipynb merged.ipynb
nbutils diff ours.ipynb merged.ipynb
```

### 4. Test Merged Notebook

```bash
# Execute to verify it works
nbutils run merged.ipynb
```

## Related Commands

- [`git-setup`](git-setup.md) - Configure automatic resolve in git
- [`diff`](diff.md) - Compare notebooks before/after merge
- [`combine`](combine.md) - Simple concatenation (no conflict detection)
- [`clean`](clean.md) - Clean notebooks before merging

## See Also

- [Examples](../examples/resolve.md) - Practical usage examples
- [nbdime documentation](https://nbdime.readthedocs.io/) - Learn about nbdime
- [Getting Started](../getting-started/welcome.md) - Introduction to nbutils

