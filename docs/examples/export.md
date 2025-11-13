# Export Command Examples

Practical examples for using `nbctl export` to convert notebooks.

## Basic Export

### Export to HTML

```bash
nbctl export analysis.ipynb -f html
```

**Result:** `analysis.html` created.

---

### Export to PDF

```bash
nbctl export report.ipynb -f pdf
```

**Requires:** LaTeX installation.

---

### Export to Python

```bash
nbctl export notebook.ipynb -f py
```

**Result:** `notebook.py` with markdown as comments.

---

### Export to Markdown

```bash
nbctl export notebook.ipynb -f md
```

---

## Multiple Formats

### Export to Multiple Formats

```bash
nbctl export analysis.ipynb -f html,pdf,py,md
```

**Creates:**
- `analysis.html`
- `analysis.pdf`
- `analysis.py`
- `analysis.md`

---

### Reports Package

Export complete report package:

```bash
nbctl export quarterly_report.ipynb -f html,pdf --output-dir reports/q4/
```

---

## Export Options

### Without Input Cells

Create output-only report (for non-technical audiences):

```bash
nbctl export report.ipynb -f html --no-input
```

**Result:** HTML with only outputs and markdown (no code).

---

### Without Prompts

Clean export without `In[1]:` / `Out[1]:`:

```bash
nbctl export notebook.ipynb -f html --no-prompt
```

---

### Combined Options

```bash
nbctl export presentation.ipynb -f html --no-input --no-prompt
```

Perfect for stakeholder presentations.

---

## Workflow Examples

### Generate Reports

Automated report generation:

```bash
#!/bin/bash
# generate-reports.sh

# 1. Run notebook to update outputs
nbctl run analysis.ipynb --save-output ./executed/

# 2. Export executed notebook
nbctl export ./executed/analysis.ipynb -f html,pdf --output-dir ./reports/

# 3. Share reports
echo "Reports generated in ./reports/"
```

---

### Weekly Report Automation

```bash
#!/bin/bash
# weekly-report.sh

date=$(date +%Y-%m-%d)
report_dir="reports/week-$date"

mkdir -p "$report_dir"

for nb in analysis/*.ipynb; do
    name=$(basename "$nb" .ipynb)
    nbctl export "$nb" -f html,pdf --output-dir "$report_dir/"
done

echo "Weekly reports generated in $report_dir"
```

---

### Documentation Generation

Generate docs from notebooks:

```bash
#!/bin/bash
# Generate markdown docs from notebooks

mkdir -p docs/tutorials

for nb in tutorials/*.ipynb; do
    nbctl export "$nb" -f md --output-dir docs/tutorials/
done

echo "Documentation generated"
```

---

## Presentation Examples

### Create Slides

```bash
nbctl export presentation.ipynb -f slides
```

**Result:** `presentation.html` (Reveal.js slides).

---

### Presentation Package

```bash
# Create full presentation package
nbctl export talk.ipynb -f slides,pdf --no-prompt
```

---

## Batch Export

### Export All Notebooks

```bash
for nb in *.ipynb; do
    nbctl export "$nb" -f html
done
```

---

### Export by Category

```bash
# Export analysis notebooks to HTML
for nb in analysis_*.ipynb; do
    nbctl export "$nb" -f html --output-dir html/
done

# Export model notebooks to Python
for nb in model_*.ipynb; do
    nbctl export "$nb" -f py --output-dir python/
done
```

---

## Advanced Examples

### Conditional Export

Export only if newer than existing HTML:

```bash
nb="analysis.ipynb"
html="analysis.html"

if [ "$nb" -nt "$html" ]; then
    nbctl export "$nb" -f html
    echo "Updated $html"
else
    echo "$html is up to date"
fi
```

---

### Export with Post-Processing

```bash
# Export and customize
nbctl export notebook.ipynb -f html

# Add custom CSS
cat custom-style.css >> notebook.html
```

---

### Archive Export

Create timestamped archive:

```bash
#!/bin/bash
date=$(date +%Y%m%d-%H%M%S)
archive_dir="exports/$date"

mkdir -p "$archive_dir"

nbctl export notebook.ipynb -f html,pdf,py --output-dir "$archive_dir/"

echo "Archived to $archive_dir"
```

---

## CI/CD Examples

### GitHub Actions

`.github/workflows/export-notebooks.yml`:

```yaml
name: Export Notebooks
on: [push]

jobs:
  export:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Setup Python
        uses: actions/setup-python@v2
        
      - name: Install dependencies
        run: |
          pip install nbctl
          sudo apt-get install texlive-xetex
      
      - name: Export notebooks
        run: |
          mkdir -p exports
          for nb in *.ipynb; do
            nbctl export "$nb" -f html,pdf --output-dir exports/
          done
      
      - name: Upload artifacts
        uses: actions/upload-artifact@v2
        with:
          name: notebooks-export
          path: exports/
```

---

## Tips & Best Practices

### 1. Test Exports

```bash
# Test HTML export first (fastest)
nbctl export notebook.ipynb -f html

# If OK, export to PDF
nbctl export notebook.ipynb -f pdf
```

### 2. Organize Outputs

```bash
# Organize by format
nbctl export notebook.ipynb -f html --output-dir html/
nbctl export notebook.ipynb -f pdf --output-dir pdf/
nbctl export notebook.ipynb -f py --output-dir python/
```

### 3. Clean Before Export

```bash
# Clean and run before export
nbctl clean notebook.ipynb
nbctl run notebook.ipynb
nbctl export notebook.ipynb -f html,pdf
```

---

## Troubleshooting

### PDF Export Fails

Install LaTeX:

```bash
# macOS
brew install --cask mactex

# Ubuntu
sudo apt-get install texlive-xetex texlive-fonts-recommended
```

---

## Related Examples

- [Run Examples](run.md) - Execute before exporting
- [Extract Examples](extract.md) - Extract specific outputs
- [Clean Examples](clean.md) - Clean before export

