# Extract Command Examples

Practical examples for using `nbctl extract` to save notebook outputs.

## Basic Usage

### Extract All Outputs (Interactive)

```bash
nbctl extract analysis.ipynb
```

**Prompts:**
```
What would you like to extract?
1. Both data and images
2. Only data outputs
3. Only image outputs
4. All outputs without prompting

Enter choice (1-4):
```

---

### Extract Everything (Non-Interactive)

```bash
nbctl extract analysis.ipynb --all
```

**Result:**
```
outputs/
├── data/
│   └── cell_0_output_0_data_0.json
└── images/
    ├── cell_2_output_0_img_0.png
    └── cell_5_output_0_img_1.svg
```

---

### Extract Only Images

```bash
nbctl extract analysis.ipynb --images
```

Perfect for saving plots and visualizations.

---

### Extract Only Data

```bash
nbctl extract analysis.ipynb --data
```

Perfect for saving DataFrames and JSON outputs.

---

## Custom Output Directory

### Save to Custom Location

```bash
nbctl extract notebook.ipynb --all -o ./figures/
```

---

### Organized Extraction

```bash
# Extract images to figures directory
nbctl extract analysis.ipynb --images -o ./report/figures/

# Extract data to data directory
nbctl extract analysis.ipynb --data -o ./report/data/
```

---

## Workflow Examples

### Create Report Package

Extract outputs for a report:

```bash
#!/bin/bash
# create-report-package.sh

notebook="analysis.ipynb"
report_dir="report-$(date +%Y%m%d)"

mkdir -p "$report_dir"

# Extract all outputs
nbctl extract "$notebook" --all -o "$report_dir/outputs/"

# Export to HTML
nbctl export "$notebook" -f html --output-dir "$report_dir/"

# Create archive
tar -czf "$report_dir.tar.gz" "$report_dir"

echo "Report package: $report_dir.tar.gz"
```

---

### Extract for Publication

Save figures for academic paper:

```bash
# Create publication-ready figures directory
mkdir -p paper/figures

# Extract all plots
nbctl extract ml_results.ipynb --images -o paper/figures/

# Rename for paper
cd paper/figures
mv cell_3_output_0_img_0.png figure1_accuracy.png
mv cell_7_output_0_img_1.png figure2_confusion_matrix.png
```

---

### Batch Extraction

Extract from multiple notebooks:

```bash
#!/bin/bash
# Extract outputs from all analysis notebooks

for nb in analysis_*.ipynb; do
    name=$(basename "$nb" .ipynb)
    nbctl extract "$nb" --all -o "outputs/$name/"
done

echo "Extracted outputs from all notebooks"
```

---

## Data Extraction Examples

### Save DataFrames

Extract pandas DataFrame HTML tables:

```bash
nbctl extract data_analysis.ipynb --data
```

**Result:** DataFrames saved as HTML tables.

---

### Extract JSON Results

Save model evaluation metrics:

```bash
nbctl extract ml_training.ipynb --data -o results/

# results/data/ contains JSON files with metrics
```

---

### Extract CSV Data

```bash
nbctl extract processing.ipynb --data

# CSVoutputs saved as .csv files
```

---

## Image Extraction Examples

### Save All Plots

Extract matplotlib/seaborn plots:

```bash
nbctl extract visualization.ipynb --images -o plots/
```

---

### Save Vector Graphics

Extract SVG for scalable figures:

```bash
nbctl extract notebook.ipynb --images -o figures/

# Look for .svg files in figures/images/
```

---

### Extract for Presentation

```bash
# Extract plots for slides
nbctl extract analysis.ipynb --images -o presentation/images/

# Use in PowerPoint, Google Slides, etc.
```

---

## Advanced Examples

### Conditional Extraction

Extract only if outputs exist:

```bash
if nbctl info notebook.ipynb | grep -q "outputs"; then
    nbctl extract notebook.ipynb --all
    echo "Outputs extracted"
else
    echo "ℹ No outputs to extract"
fi
```

---

### Extract with Timestamp

```bash
timestamp=$(date +%Y%m%d-%H%M%S)
nbctl extract notebook.ipynb --all -o "outputs-$timestamp/"
```

---

### Extract and Archive

```bash
# Extract outputs
nbctl extract notebook.ipynb --all -o temp-outputs/

# Create archive
tar -czf outputs-$(date +%Y%m%d).tar.gz temp-outputs/

# Cleanup
rm -rf temp-outputs/

echo "Outputs archived"
```

---

## Automated Workflows

### Daily Plot Extraction

```bash
#!/bin/bash
# daily-plots.sh - Extract plots daily

date=$(date +%Y-%m-%d)
plot_dir="plots/$date"

mkdir -p "$plot_dir"

for nb in dashboards/*.ipynb; do
    # Run notebook to generate latest plots
    nbctl run "$nb"
    
    # Extract plots
    name=$(basename "$nb" .ipynb)
    nbctl extract "$nb" --images -o "$plot_dir/$name/"
done

echo "Daily plots extracted to $plot_dir"
```

---

### CI/CD Integration

`.github/workflows/extract-outputs.yml`:

```yaml
name: Extract Outputs
on:
  push:
    paths:
      - '**.ipynb'

jobs:
  extract:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Setup Python
        uses: actions/setup-python@v2
        
      - name: Install nbctl
        run: pip install nbctl
      
      - name: Extract outputs
        run: |
          mkdir -p artifacts
          for nb in *.ipynb; do
            nbctl extract "$nb" --all -o "artifacts/${nb%.ipynb}/"
          done
      
      - name: Upload artifacts
        uses: actions/upload-artifact@v2
        with:
          name: notebook-outputs
          path: artifacts/
```

---

## Organization Patterns

### By Notebook

```bash
# Structure: outputs/{notebook_name}/data/ and /images/

for nb in *.ipynb; do
    name=$(basename "$nb" .ipynb)
    nbctl extract "$nb" --all -o "outputs/$name/"
done
```

**Result:**
```
outputs/
├── analysis1/
│   ├── data/
│   └── images/
└── analysis2/
    ├── data/
    └── images/
```

---

### By Date

```bash
date=$(date +%Y-%m-%d)
nbctl extract notebook.ipynb --all -o "outputs/$date/"
```

---

### By Type

```bash
# All images in one place
nbctl extract *.ipynb --images -o all-images/

# All data in one place
nbctl extract *.ipynb --data -o all-data/
```

---

## Tips & Best Practices

### 1. Run Before Extract

```bash
# Ensure latest outputs
nbctl run notebook.ipynb
nbctl extract notebook.ipynb --all
```

### 2. Organize Extraction

```bash
# Create clear structure
project/
├── notebooks/
├── outputs/
│   ├── figures/
│   └── data/
└── reports/
```

### 3. Version Outputs

```bash
# Keep versions
nbctl extract notebook.ipynb --all -o "outputs/v1/"
# ... make changes ...
nbctl extract notebook.ipynb --all -o "outputs/v2/"
```

### 4. Document Outputs

Create `outputs/README.md`:

```markdown
# Outputs

Generated from: analysis.ipynb
Date: 2025-11-12

## Images
- cell_3_output_0_img_0.png: Model accuracy plot
- cell_7_output_0_img_1.png: Confusion matrix

## Data
- cell_1_output_0_data_0.json: Model metrics
```

---

## Related Examples

- [Export Examples](export.md) - Export entire notebook
- [Run Examples](run.md) - Execute to generate outputs
- [ML-Split Examples](ml-split.md) - Extract code structure

