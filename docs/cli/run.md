# nbctl run

Execute Jupyter notebooks from the command line.

## Description

The `run` command executes one or more Jupyter notebooks programmatically, without opening Jupyter. It's perfect for automation, CI/CD pipelines, batch processing, and long-running ML training jobs.

Use this command to:
- Execute notebooks in CI/CD pipelines
- Run ML training notebooks overnight
- Batch process multiple notebooks
- Automate report generation
- Test notebook execution
- Generate outputs programmatically

## Usage

```bash
nbctl run NOTEBOOK [NOTEBOOK...] [OPTIONS]
```

## Arguments

| Argument | Description | Required |
|----------|-------------|----------|
| `NOTEBOOK` | Path(s) to Jupyter notebook file(s) | Yes (1 or more) |

## Options

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `--order` | | Flag | False | Run notebooks in alphabetical order |
| `--timeout` | `-t` | INT | None | Timeout per cell in seconds |
| `--allow-errors` | | Flag | False | Continue execution if cells fail |
| `--save-output` | `-o` | PATH | None | Directory to save executed notebooks |
| `--kernel` | `-k` | TEXT | `python3` | Kernel name to use for execution |

## Execution Behavior

### Default Behavior
- Notebooks run in the order specified on command line
- Execution stops if any cell raises an error
- No timeout (cells can run indefinitely)
- Original notebooks are NOT modified

### With `--order`
- Notebooks run in alphabetical order regardless of command-line order
- Useful with wildcards: `nbctl run *.ipynb --order`

### With `--timeout`
- Each cell must complete within the specified seconds
- Prevents infinite loops or hanging cells
- Useful for testing and CI/CD

### With `--allow-errors`
- Execution continues even if cells fail
- Failed cells are logged but don't stop execution
- Useful for partial execution or testing

### With `--save-output`
- Executed notebooks (with outputs) saved to specified directory
- Original notebooks remain unchanged
- Useful for generating reports or archiving results

## Output

### Execution Progress

```
Running: notebook1.ipynb
  Cell 1/10 ✓
  Cell 2/10 ✓
  Cell 3/10 ✓
  ...
  Cell 10/10 ✓
Completed: notebook1.ipynb (5.2s)

Running: notebook2.ipynb
  Cell 1/15 ✓
  ...
```

### Execution Summary

```
Execution Summary

┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━┓
┃ Notebook         ┃ Status  ┃ Time  ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━┩
│ 01_load.ipynb    │ Success │ 2.3s  │
│ 02_process.ipynb │ Success │ 5.1s  │
│ 03_analyze.ipynb │ Success │ 3.7s  │
└──────────────────┴─────────┴───────┘

Total: 3 notebooks | Successful: 3 | Failed: 0 | Total time: 11.1s
```

### Error Output

```
Running: notebook.ipynb
  Cell 1/10 ✓
  Cell 2/10 Error

Error in cell 2:
  NameError: name 'undefined_var' is not defined

Execution failed: notebook.ipynb
```

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | All notebooks executed successfully |
| 1 | One or more notebooks failed |
| 2 | File not found or invalid notebook |
| 3 | Kernel not found |

## Kernel Selection

Available kernels depend on your Jupyter installation:

```bash
# List available kernels
jupyter kernelspec list

# Use specific kernel
nbctl run notebook.ipynb --kernel python3
nbctl run notebook.ipynb --kernel ir  # R kernel
```

Common kernel names:
- `python3` - Python 3 (default)
- `python2` - Python 2 (if installed)
- `ir` - R
- `julia` - Julia

## Timeout Behavior

### No Timeout (Default)
- Cells can run indefinitely
- Good for long-running ML training
- Risk: May hang on infinite loops

### With Timeout
```bash
nbctl run notebook.ipynb --timeout 600  # 10 minutes per cell
```
- Each cell must complete within specified seconds
- TimeoutError raised if cell exceeds limit
- Execution stops (unless `--allow-errors` used)

### Recommended Timeouts

| Use Case | Timeout | Rationale |
|----------|---------|-----------|
| Quick analysis | 60s | Fast feedback |
| Data processing | 300s (5min) | Reasonable for most tasks |
| ML training | None | May take hours |
| CI/CD testing | 120s | Prevent hanging builds |

## Saving Outputs

### Without `--save-output`
- Notebooks executed in memory
- Original files unchanged
- Outputs discarded after execution

### With `--save-output`
```bash
nbctl run analysis.ipynb --save-output ./executed/
```
- Executed notebooks saved with all outputs
- Original notebooks unchanged
- Directory structure preserved

Output:
```
executed/
└── analysis.ipynb  # With all cell outputs
```

## Multiple Notebooks

### Specified Order
```bash
nbctl run 01_load.ipynb 02_process.ipynb 03_analyze.ipynb
```
Runs in the order: 01 → 02 → 03

### Alphabetical Order
```bash
nbctl run *.ipynb --order
```
Runs in alphabetical order automatically

### With Wildcards
```bash
# All notebooks in directory
nbctl run *.ipynb

# Specific pattern
nbctl run analysis_*.ipynb

# Multiple patterns (shell expansion)
nbctl run data_*.ipynb model_*.ipynb
```

## Notes

- **Read-only by default:** Original notebooks not modified unless `--save-output` used
- **Isolated execution:** Each notebook runs independently
- **No shared state:** Notebooks don't share variables
- **Kernel per notebook:** Each notebook gets a fresh kernel instance
- **Working directory:** Notebooks execute in their containing directory
- **Environment variables:** Inherited from shell environment

## Common Use Cases

### CI/CD Pipeline Testing
```bash
# Quick test with timeout
nbctl run tests/*.ipynb --timeout 120 --allow-errors
```

### ML Training Pipeline
```bash
# No timeout for long training
nbctl run 01_preprocess.ipynb 02_train.ipynb 03_evaluate.ipynb
```

### Report Generation
```bash
# Generate reports with outputs
nbctl run reports/*.ipynb --save-output ./generated_reports/
```

### Batch Processing
```bash
# Process all analysis notebooks
nbctl run analysis_*.ipynb --order
```

## Performance Considerations

- **Memory usage:** Each notebook execution consumes memory
- **Parallel execution:** Not supported (run notebooks sequentially)
- **Large notebooks:** May take significant time and memory
- **Output size:** Large outputs increase execution time

## Error Handling

### Stop on First Error (Default)
```bash
nbctl run nb1.ipynb nb2.ipynb nb3.ipynb
# If nb2 fails, nb3 is not executed
```

### Continue on Errors
```bash
nbctl run nb1.ipynb nb2.ipynb nb3.ipynb --allow-errors
# All notebooks attempted even if some fail
# Exit code reflects failures
```

## Related Commands

- [`clean`](clean.md) - Clean notebooks before/after execution
- [`ml-split`](ml-split.md) - Convert notebooks to runnable Python
- [`info`](info.md) - Analyze notebooks before running
- [`export`](export.md) - Export executed notebooks to formats

## See Also

- [Examples](../examples/run.md) - Practical usage examples
- [Getting Started](../getting-started/welcome.md) - Introduction to nbctl

