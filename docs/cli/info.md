# nbctl info

Display comprehensive notebook statistics and analysis.

## Description

The `info` command provides detailed insights about your Jupyter notebook including cell counts, file size, code metrics, complexity, and all import statements.

Use this command to:
- Understand notebook structure
- Track code complexity
- Identify dependencies
- Analyze code metrics
- Plan refactoring

## Usage

```bash
nbctl info NOTEBOOK [OPTIONS]
```

## Arguments

| Argument | Description | Required |
|----------|-------------|----------|
| `NOTEBOOK` | Path to the Jupyter notebook file | Yes |

## Options

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `--code-metrics` | | Flag | False | Show only code metrics |
| `--imports` | | Flag | False | Show only import statements |

## Output

### Default Output (All Information)

```
Notebook Information: notebook.ipynb

Basic Statistics:
- Total cells: 25
- Code cells: 18
- Markdown cells: 6
- Raw cells: 1
- File size: 145.2 KB

Code Metrics:
- Total lines of code: 234
- Average lines per cell: 13.0
- Empty code cells: 2
- Code complexity: Medium

Dependencies:
- numpy
- pandas
- matplotlib.pyplot
- sklearn.model_selection
- sklearn.ensemble
```

### Code Metrics Only (`--code-metrics`)

```
Code Metrics:
- Total lines of code: 234
- Average lines per cell: 13.0
- Empty code cells: 2
- Code complexity: Medium
```

### Imports Only (`--imports`)

```
Dependencies:
- numpy
- pandas
- matplotlib.pyplot as plt
- sklearn.model_selection.train_test_split
- sklearn.ensemble.RandomForestClassifier
```

## Metrics Explained

### Code Complexity Levels

| Level | Criteria | Recommendation |
|-------|----------|----------------|
| **Low** | < 50 lines, simple structure | Good for learning/prototyping |
| **Medium** | 50-200 lines, moderate structure | Typical notebook |
| **High** | 200-500 lines, complex structure | Consider splitting |
| **Very High** | > 500 lines | Strongly consider splitting |

### Cell Statistics

- **Total cells:** All cells in notebook
- **Code cells:** Executable Python cells
- **Markdown cells:** Documentation cells
- **Raw cells:** Unformatted cells

### Code Metrics

- **Total lines:** Sum of all lines in code cells (excluding empty lines)
- **Average lines per cell:** Mean lines per code cell
- **Empty code cells:** Code cells with no content

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | File not found or invalid notebook |
| 2 | Permission error |

## Notes

- **Fast analysis:** Parses notebook structure without execution
- **No modifications:** Read-only operation, never modifies notebook
- **Import detection:** Captures all import types (import, from...import, as)
- **Use for planning:** Helps decide when to split or refactor notebooks

## Related Commands

- [`lint`](lint.md) - Check code quality issues
- [`ml-split`](ml-split.md) - Split large notebooks into modules
- [`clean`](clean.md) - Prepare notebooks for analysis

## See Also

- [Examples](../examples/info.md) - Practical usage examples
- [Getting Started](../getting-started/welcome.md) - Introduction to nbctl

