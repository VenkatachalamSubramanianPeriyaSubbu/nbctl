# nbctl lint

Check code quality and identify issues in notebooks.

## Description

The `lint` command analyzes Jupyter notebooks for code quality issues, best practices violations, and potential problems. It helps maintain clean, readable, and maintainable notebook code.

Use this command to:
- Identify unused imports
- Find overly long cells
- Detect empty code cells
- Check for code quality issues
- Enforce coding standards
- Maintain team consistency

## Usage

```bash
nbctl lint NOTEBOOK [OPTIONS]
```

## Arguments

| Argument | Description | Required |
|----------|-------------|----------|
| `NOTEBOOK` | Path to the Jupyter notebook file | Yes |

## Options

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `--max-cell-length` | | INT | 100 | Maximum lines per cell before warning |

## Checks Performed

### 1. Unused Imports
Detects import statements that are never used in the code.

**Example:**
```python
import pandas as pd  # Used
import numpy as np   # Unused ← Flagged
import matplotlib.pyplot as plt  # Used
```

**Why it matters:**
- Clutters code
- Increases load time
- Confuses readers about dependencies

---

### 2. Overly Long Cells
Identifies code cells that exceed the maximum length threshold.

**Default threshold:** 100 lines per cell

**Why it matters:**
- Hard to read and understand
- Difficult to debug
- Should be split into smaller cells
- Indicates need for refactoring

---

### 3. Empty Code Cells
Finds code cells with no content.

**Why it matters:**
- Creates clutter in notebook
- Can be confusing during review
- Serves no purpose
- Should be removed

---

### 4. Code Quality Issues
Additional checks for Python code quality:
- Syntax errors
- Undefined variables (basic check)
- Inconsistent indentation
- Line length issues

## Output

### Clean Notebook (No Issues)

```
Linting completed: notebook.ipynb

No issues found!
```

### Notebook with Issues

```
Linting notebook.ipynb

Issues found:

Unused Imports:
  Cell 1:
    - numpy (imported as np)
    - matplotlib.pyplot
  Cell 5:
    - json

Overly Long Cells:
  Cell 8: 145 lines (max: 100)
    Consider splitting into smaller cells
  Cell 12: 127 lines (max: 100)
    Consider splitting into smaller cells

Empty Code Cells:
  Cell 3
  Cell 7
  Cell 15

Summary:
  - 3 unused imports
  - 2 overly long cells
  - 3 empty cells
  
Total: 8 issues found
```

## Severity Levels

Issues are categorized by severity:

| Severity | Description | Examples |
|----------|-------------|----------|
| **ERROR** | Must be fixed | Syntax errors |
| **WARNING** | Should be fixed | Unused imports, long cells |
| **INFO** | Consider fixing | Empty cells |

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | No issues found |
| 1 | Issues found (warnings/errors) |
| 2 | File not found or invalid notebook |

## Configuring Thresholds

### Cell Length Threshold

Adjust the maximum cell length based on your team's standards:

```bash
# Stricter (shorter cells)
nbctl lint notebook.ipynb --max-cell-length 50

# More lenient (longer cells)
nbctl lint notebook.ipynb --max-cell-length 150

# Very strict
nbctl lint notebook.ipynb --max-cell-length 30
```

**Recommendations:**

| Project Type | Threshold | Rationale |
|--------------|-----------|-----------|
| Teaching/Tutorial | 30-50 | Small, digestible chunks |
| Analysis | 50-100 | Balance between readability and flow |
| Research | 100-150 | More complex operations acceptable |
| Production | 50-75 | Strict standards for maintainability |

## Notes

- **Read-only:** Never modifies the notebook
- **Static analysis:** Doesn't execute code
- **Import detection:** Checks all import types (import, from...import)
- **Usage tracking:** Scans all code cells for import usage
- **No auto-fix:** Only reports issues (use `format` for auto-fixing some issues)

## Best Practices

### Fixing Unused Imports
Remove imports that aren't used:

```python
# Before
import pandas as pd
import numpy as np
import json

# After (json removed if unused)
import pandas as pd
import numpy as np
```

### Fixing Long Cells
Split into multiple smaller cells:

```python
# Before: One 150-line cell
# [lots of code...]

# After: Multiple focused cells
# Cell 1: Load data (20 lines)
# Cell 2: Clean data (30 lines)
# Cell 3: Transform data (40 lines)
# Cell 4: Analyze data (30 lines)
```

### Fixing Empty Cells
Simply delete empty code cells in Jupyter or use:
- Edit → Delete Cells
- Keyboard: `dd` in command mode

## Integration with CI/CD

Use in continuous integration to enforce standards:

```bash
# Fail build if issues found
nbctl lint notebook.ipynb || exit 1

# Lint all notebooks
for nb in *.ipynb; do
    nbctl lint "$nb" || exit 1
done

# Custom threshold for project
nbctl lint notebook.ipynb --max-cell-length 75 || exit 1
```

## Comparison with format

| Command | Purpose | Modifies Files | Use Case |
|---------|---------|----------------|----------|
| **lint** | Find issues | No | Quality checks, CI/CD |
| **format** | Fix style | Yes | Auto-formatting code |

**Typical workflow:**
1. Run `lint` to find issues
2. Manually fix structural issues (long cells, unused imports)
3. Run `format` to fix code style
4. Run `lint` again to verify

## Related Commands

- [`format`](format.md) - Auto-format code with black
- [`info`](info.md) - Get notebook statistics and metrics
- [`security`](security.md) - Check for security vulnerabilities
- [`clean`](clean.md) - Clean notebooks for git

## See Also

- [Examples](../examples/lint.md) - Practical usage examples
- [Getting Started](../getting-started/welcome.md) - Introduction to nbutils

