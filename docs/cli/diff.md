# nbctl diff

Compare notebooks intelligently (ignores outputs and metadata).

## Description

The `diff` command compares two Jupyter notebooks and shows you the differences in a meaningful way. Unlike `git diff` which shows JSON changes, nbctl diff focuses on actual code changes and ignores outputs, execution counts, and metadata.

Use this command to:
- Review changes between notebook versions
- Compare notebooks before merging
- Understand what code actually changed
- Create meaningful code reviews
- Track notebook evolution

## Usage

```bash
nbctl diff NOTEBOOK1 NOTEBOOK2 [OPTIONS]
```

## Arguments

| Argument | Description | Required |
|----------|-------------|----------|
| `NOTEBOOK1` | Path to first notebook (base/old version) | Yes |
| `NOTEBOOK2` | Path to second notebook (new version) | Yes |

## Options

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `--format` | `-f` | TEXT | `table` | Output format: `table`, `unified`, `json` |
| `--code-only` | | Flag | False | Show only code cell changes |
| `--stats` | | Flag | False | Show only statistics |

## Output Formats

### Table Format (Default)

Human-readable table showing differences:

```bash
nbctl diff old.ipynb new.ipynb
```

Output:
```
Notebook Diff: old.ipynb → new.ipynb

┏━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Cell # ┃ Type     ┃ Change                       ┃
┡━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 1      │ Code     │ Modified                     │
│ 2      │ Code     │ Unchanged                    │
│ 3      │ Markdown │ Modified                     │
│ 4      │ Code     │ Added                        │
│ 5      │ Code     │ Deleted                      │
└────────┴──────────┴──────────────────────────────┘

Summary:
  - Modified: 2 cells
  - Added: 1 cell
  - Deleted: 1 cell
  - Unchanged: 1 cell
```

---

### Unified Format

Git-style unified diff showing line-by-line changes:

```bash
nbctl diff old.ipynb new.ipynb --format unified
```

Output:
```
--- old.ipynb
+++ new.ipynb

Cell 1 (Code):
@@ -1,3 +1,3 @@
 import pandas as pd
-import numpy as np
+import numpy as np
 import matplotlib.pyplot as plt

Cell 3 (Markdown):
@@ -1,1 +1,2 @@
 # Data Analysis
+## Updated Analysis

Cell 4 (Code) - Added:
+ # New cell
+ df = pd.read_csv('new_data.csv')

Cell 5 (Code) - Deleted:
- old_variable = 123
- print(old_variable)
```

---

### JSON Format

Machine-readable JSON for automation:

```bash
nbctl diff old.ipynb new.ipynb --format json
```

Output:
```json
{
  "notebook1": "old.ipynb",
  "notebook2": "new.ipynb",
  "changes": [
    {
      "cell_index": 1,
      "cell_type": "code",
      "change_type": "modified",
      "old_content": "import pandas as pd\nimport numpy as np",
      "new_content": "import pandas as pd\nimport numpy as np\nimport sklearn"
    },
    {
      "cell_index": 4,
      "cell_type": "code",
      "change_type": "added",
      "new_content": "df = pd.read_csv('data.csv')"
    }
  ],
  "summary": {
    "modified": 1,
    "added": 1,
    "deleted": 0,
    "unchanged": 10
  }
}
```

## Filter Options

### Code Only

Show only changes to code cells (ignore markdown):

```bash
nbctl diff old.ipynb new.ipynb --code-only
```

**Use case:** Focus on code changes for technical review.

---

### Statistics Only

Show summary statistics without detailed changes:

```bash
nbctl diff old.ipynb new.ipynb --stats
```

Output:
```
Diff Statistics: old.ipynb → new.ipynb

Cells:
  - Total in notebook1: 12
  - Total in notebook2: 13
  - Modified: 2
  - Added: 1
  - Deleted: 0
  - Unchanged: 10

Lines of Code:
  - Added: 15 lines
  - Removed: 3 lines
  - Net change: +12 lines
```

## What Gets Compared

### Compared

- Source code in code cells
- Markdown cell content
- Raw cell content
- Cell order and structure
- Cell types

### Ignored

- Cell outputs (text, images, plots)
- Execution counts (In[1], Out[1])
- Cell metadata
- Notebook metadata
- Timestamps
- Kernel information

## Change Types

| Type | Description | Example |
|------|-------------|---------|
| **Modified** | Cell content changed | Code updated, markdown edited |
| **Added** | New cell in notebook2 | New cell added |
| **Deleted** | Cell removed from notebook1 | Cell deleted |
| **Unchanged** | Identical cells | No changes |

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Notebooks compared successfully |
| 1 | Files not found or invalid notebooks |
| 2 | Notebooks are identical |

## Use Cases

### Code Review

```bash
# Review changes before merging
nbctl diff main_branch.ipynb feature_branch.ipynb

# Focus on code changes
nbctl diff main.ipynb feature.ipynb --code-only
```

### Git Integration

```bash
# Compare with previous commit
git show HEAD:notebook.ipynb > /tmp/old.ipynb
nbctl diff /tmp/old.ipynb notebook.ipynb
```

### Quick Check

```bash
# Just see if there are differences
nbctl diff nb1.ipynb nb2.ipynb --stats
```

### Automation

```bash
# Parse differences programmatically
nbctl diff old.ipynb new.ipynb --format json > diff.json
python process_diff.py diff.json
```

## Comparison with git diff

| Feature | `git diff` | `nbctl diff` |
|---------|------------|----------------|
| Format | JSON changes | Source code changes |
| Outputs | Included | Ignored |
| Metadata | Included | Ignored |
| Execution counts | Included | Ignored |
| Readability | Low | High |
| Code review | Difficult | Easy |

## Performance

- **Fast:** Efficient comparison algorithm
- **Memory efficient:** Streams large notebooks
- **Large notebooks:** Handles notebooks with thousands of cells
- **Large diffs:** Can compare significantly different notebooks

## Notes

- **Read-only:** Never modifies either notebook
- **Non-destructive:** Original files remain unchanged
- **Order matters:** First file is "base", second is "new"
- **Cell IDs:** Matches cells by position, not ID
- **Fuzzy matching:** Intelligently matches similar cells

## Git Integration

When used as git diff driver (via `git-setup`):

```bash
# In .gitattributes
*.ipynb diff=nbutils

# In .git/config
[diff "nbutils"]
    command = nbctl diff
```

Then `git diff notebook.ipynb` uses nbctl automatically!

## Related Commands

- [`git-setup`](git-setup.md) - Configure git to use nbctl diff
- [`resolve`](resolve.md) - Merge notebooks with conflicts
- [`combine`](combine.md) - Concatenate notebooks
- [`clean`](clean.md) - Prepare notebooks for comparison

## See Also

- [Examples](../examples/diff.md) - Practical usage examples
- [Getting Started](../getting-started/welcome.md) - Introduction to nbutils

