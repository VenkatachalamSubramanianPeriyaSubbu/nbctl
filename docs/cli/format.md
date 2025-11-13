# nbctl format

Auto-format code cells with black.

## Description

The `format` command automatically formats all code cells in your Jupyter notebook using [black](https://github.com/psf/black), the uncompromising Python code formatter. This ensures consistent code style across your notebooks and team.

Use this command to:
- Enforce consistent code style
- Improve code readability
- Save time on manual formatting
- Maintain team coding standards
- Prepare notebooks for collaboration
- Meet PEP 8 style guidelines

## Usage

```bash
nbctl format NOTEBOOK [OPTIONS]
```

## Arguments

| Argument | Description | Required |
|----------|-------------|----------|
| `NOTEBOOK` | Path to the Jupyter notebook file | Yes |

## Options

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `--output-dir` | `-o` | PATH | In-place | Output directory for formatted notebook |
| `--line-length` | | INT | 88 | Maximum line length for formatting |

## What Gets Formatted

### Code Cells
- All Python code cells are formatted
- Proper indentation applied
- Consistent spacing
- String quote normalization
- Line length management

### Not Formatted
- Markdown cells (unchanged)
- Raw cells (unchanged)
- Cell outputs (unchanged)
- Notebook metadata (unchanged)

## Output

### Success

```
Formatting notebook.ipynb with black...

Formatted successfully
  - 15 code cells processed
  - 12 cells modified
  - 3 cells unchanged

Changes:
  Cell 2: Fixed indentation
  Cell 5: Reformatted long lines
  Cell 7: Normalized quotes
  Cell 8: Added spacing
  ...
```

### No Changes Needed

```
Formatting notebook.ipynb with black...

Already formatted correctly
  - 15 code cells checked
  - 0 cells modified

No formatting changes needed.
```

### Syntax Errors

```
Formatting notebook.ipynb with black...

Syntax error in cell 5
  Cannot format code with syntax errors
  Fix the error and try again

Error details:
  SyntaxError: invalid syntax (line 3)
```

## Formatting Examples

### Before Formatting

```python
# Cell 1: Inconsistent spacing and quotes
import pandas as pd,numpy as np
from sklearn.model_selection import train_test_split,cross_val_score

def load_data( filepath,delimiter=',' ):
    df=pd.read_csv(filepath,delimiter=delimiter)
    return df

x=[1,2,3,4,5,6,7,8,9,10]
y = [ item**2 for item in x ]
```

### After Formatting

```python
# Cell 1: Clean, consistent style
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score


def load_data(filepath, delimiter=","):
    df = pd.read_csv(filepath, delimiter=delimiter)
    return df


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [item**2 for item in x]
```

## Line Length Options

### Default (88 characters)

Black's default line length, chosen for optimal readability:

```bash
nbctl format notebook.ipynb
```

### Custom Line Length

Adjust based on your team's preferences or display constraints:

```bash
# Shorter lines (for narrow displays)
nbctl format notebook.ipynb --line-length 79

# Longer lines (for wide displays)
nbctl format notebook.ipynb --line-length 100

# Very long lines (not recommended)
nbctl format notebook.ipynb --line-length 120
```

**Recommendations:**

| Use Case | Line Length | Rationale |
|----------|-------------|-----------|
| PEP 8 strict | 79 | Traditional Python standard |
| **Black default** | **88** | **Optimal balance (recommended)** |
| Modern displays | 100 | Comfortable on modern screens |
| Code review | 79-88 | Easy to read in side-by-side diffs |

## In-Place vs. Output Directory

### In-Place Formatting (Default)

Modifies the original notebook:

```bash
nbctl format notebook.ipynb
# Modifies: notebook.ipynb
```

### Save to Different Location

Preserves original, saves formatted version elsewhere:

```bash
nbctl format notebook.ipynb --output-dir ./formatted/
# Original: notebook.ipynb (unchanged)
# Created: formatted/notebook.ipynb (formatted)
```

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success, notebook formatted |
| 1 | Syntax errors prevent formatting |
| 2 | File not found or invalid notebook |
| 3 | Permission error or I/O error |

## Black Formatting Rules

Black applies these rules automatically:

### 1. **Consistent Quotes**
Normalizes string quotes to double quotes (with exceptions):
```python
# Before
name = 'Alice'
message = "Hello"

# After
name = "Alice"
message = "Hello"
```

### 2. **Spacing**
Adds appropriate whitespace:
```python
# Before
x=5+3
def foo(a,b,c):pass

# After
x = 5 + 3
def foo(a, b, c):
    pass
```

### 3. **Line Length**
Wraps long lines:
```python
# Before
result = some_function(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

# After
result = some_function(
    arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8
)
```

### 4. **Import Formatting**
One import per line when wrapping:
```python
# Before
from sklearn.model_selection import train_test_split,cross_val_score,GridSearchCV

# After
from sklearn.model_selection import (
    train_test_split,
    cross_val_score,
    GridSearchCV,
)
```

### 5. **Trailing Commas**
Adds trailing commas in multi-line structures:
```python
# After
my_list = [
    1,
    2,
    3,
]
```

## Notes

- **Opinionated:** Black makes formatting decisions for you (no configuration)
- **Deterministic:** Same code always formats the same way
- **Fast:** Processes notebooks quickly
- **Safe:** Won't format code with syntax errors
- **Preserves semantics:** Never changes what code does, only how it looks
- **PEP 8 compatible:** Mostly compatible (with some differences)

## Best Practices

### 1. Format Before Committing
```bash
# Pre-commit workflow
nbctl format notebook.ipynb
nbctl lint notebook.ipynb
git add notebook.ipynb
git commit -m "Add analysis notebook"
```

### 2. Team Standards
```bash
# Use consistent line length across team
nbctl format *.ipynb --line-length 88
```

### 3. Format + Clean
```bash
# Format and clean for git
nbctl format notebook.ipynb
nbctl clean notebook.ipynb
```

### 4. Batch Formatting
```bash
# Format all notebooks in project
for nb in *.ipynb; do
    nbctl format "$nb"
done
```

## Integration with CI/CD

Check formatting in continuous integration:

```bash
# Check if formatting is needed (black --check)
black --check notebook.ipynb || echo "Run nbctl format"

# Or just format in CI
nbctl format notebook.ipynb
git diff --exit-code || echo "Formatting changes needed"
```

## Comparison with lint

| Command | Purpose | Modifies Files | Checks |
|---------|---------|----------------|--------|
| **format** | Fix code style | Yes | Formatting only |
| **lint** | Find issues | No | Unused imports, long cells, quality |

**Complementary tools:**
- `format` fixes style issues automatically
- `lint` finds structural and quality issues
- Use both for comprehensive code quality

## Related Commands

- [`lint`](lint.md) - Check code quality issues
- [`clean`](clean.md) - Clean notebooks for git
- [`info`](info.md) - Analyze notebook metrics
- [`git-setup`](git-setup.md) - Configure git integration

## See Also

- [Examples](../examples/format.md) - Practical usage examples
- [Black documentation](https://black.readthedocs.io/) - Learn more about black
- [Getting Started](../getting-started/welcome.md) - Introduction to nbutils

