# Info Command Examples

Practical examples for using `nbutils info` to analyze notebooks.

## Basic Usage

### Get Full Analysis

Display complete notebook information:

```bash
nbutils info analysis.ipynb
```

**Output:**
```
Notebook Information: analysis.ipynb

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
```

---

### Show Only Code Metrics

```bash
nbutils info analysis.ipynb --code-metrics
```

---

### Show Only Imports

```bash
nbutils info analysis.ipynb --imports
```

---

## Analysis Examples

### Analyze Before Splitting

Check if notebook should be split into modules:

```bash
nbutils info large_notebook.ipynb --code-metrics
```

If complexity is "Very High", consider using `ml-split`.

---

### Check Dependencies

List all notebook dependencies:

```bash
nbutils info notebook.ipynb --imports > dependencies.txt
```

---

### Batch Analysis

Analyze all notebooks in a directory:

```bash
for nb in *.ipynb; do
    echo "=== $nb ==="
    nbutils info "$nb" --code-metrics
    echo
done
```

---

### Compare Notebooks

Compare statistics of multiple notebooks:

```bash
echo "Notebook,Cells,Code Lines,Complexity"
for nb in *.ipynb; do
    info=$(nbutils info "$nb" --code-metrics)
    # Parse and format as CSV
    echo "$nb,$info"
done > notebook-stats.csv
```

---

### Find Large Notebooks

Find notebooks with many cells:

```bash
for nb in *.ipynb; do
    cells=$(nbutils info "$nb" | grep "Total cells" | awk '{print $3}')
    if [ "$cells" -gt 50 ]; then
        echo "$nb has $cells cells (consider splitting)"
    fi
done
```

---

### Track Notebook Growth

Monitor notebook size over time:

```bash
#!/bin/bash
# track-size.sh

nb="$1"
date=$(date +%Y-%m-%d)
cells=$(nbutils info "$nb" | grep "Total cells" | awk '{print $3}')
lines=$(nbutils info "$nb" | grep "lines of code" | awk '{print $5}')

echo "$date,$cells,$lines" >> notebook-growth.csv
```

---

## CI/CD Examples

### Enforce Notebook Size Limits

```bash
#!/bin/bash
# Fail CI if notebook is too large

max_cells=100

for nb in *.ipynb; do
    cells=$(nbutils info "$nb" | grep "Total cells" | awk '{print $3}')
    if [ "$cells" -gt "$max_cells" ]; then
        echo "ERROR: $nb has $cells cells (max: $max_cells)"
        exit 1
    fi
done

echo "All notebooks within size limits"
```

---

### Generate Notebook Report

```bash
#!/bin/bash
# Generate HTML report of all notebooks

echo "<html><body><h1>Notebook Report</h1>" > report.html

for nb in *.ipynb; do
    echo "<h2>$nb</h2><pre>" >> report.html
    nbutils info "$nb" >> report.html
    echo "</pre>" >> report.html
done

echo "</body></html>" >> report.html
```

---

## Tips & Best Practices

### 1. Regular Analysis

Check notebooks regularly for growth:

```bash
# Weekly check
nbutils info *.ipynb --code-metrics
```

### 2. Before Refactoring

Always analyze before splitting:

```bash
nbutils info notebook.ipynb
# If Very High complexity, refactor
```

### 3. Document Dependencies

Export dependencies for documentation:

```bash
nbutils info notebook.ipynb --imports > DEPENDENCIES.md
```

---

## Related Examples

- [ML-Split Examples](ml-split.md) - Split large notebooks
- [Lint Examples](lint.md) - Check code quality
- [Clean Examples](clean.md) - Clean before analysis

