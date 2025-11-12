# nbutils export

Convert notebooks to multiple formats simultaneously.

## Description

The `export` command converts Jupyter notebooks to various output formats including HTML, PDF, Markdown, Python scripts, LaTeX, and more. You can export to multiple formats in a single command.

Use this command to:
- Generate reports (HTML, PDF)
- Create documentation (Markdown)
- Extract code (Python scripts)
- Create presentations (Slides)
- Share results with non-technical stakeholders

## Usage

```bash
nbutils export NOTEBOOK --format FORMATS [OPTIONS]
```

## Arguments

| Argument | Description | Required |
|----------|-------------|----------|
| `NOTEBOOK` | Path to the Jupyter notebook file | Yes |

## Options

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `--format` | `-f` | TEXT | Required | Output formats (comma-separated) |
| `--output-dir` | `-o` | PATH | Current dir | Output directory for exported files |
| `--no-input` | | Flag | False | Exclude input cells (code) |
| `--no-prompt` | | Flag | False | Exclude cell prompts (In[1], Out[1]) |

## Supported Formats

| Format | Extension | Description | Requirements |
|--------|-----------|-------------|--------------|
| `html` | .html | HTML document | None |
| `pdf` | .pdf | PDF document | LaTeX (pdflatex) |
| `markdown`, `md` | .md | Markdown document | None |
| `python`, `py` | .py | Python script | None |
| `latex`, `tex` | .tex | LaTeX document | None |
| `rst` | .rst | reStructuredText | None |
| `slides` | .html | Reveal.js presentation | None |

## Output

Exported files are saved with the notebook's base name and appropriate extension:

```
notebook.ipynb → exports/
├── notebook.html
├── notebook.pdf
├── notebook.md
└── notebook.py
```

### Success Message

```
Exported to HTML: notebook.html
Exported to PDF: notebook.pdf
Exported to Markdown: notebook.md

3 formats exported successfully
```

### Error Messages

```
PDF export failed: pdflatex not found
  Install LaTeX to enable PDF export
```

## PDF Export Requirements

PDF export requires LaTeX to be installed:

### macOS
```bash
brew install --cask mactex
```

### Linux (Ubuntu/Debian)
```bash
sudo apt-get install texlive-xetex texlive-fonts-recommended
```

### Windows
Download and install [MiKTeX](https://miktex.org/)

## Output Options

### Standard Output
Includes both input cells (code) and output cells (results).

### No Input (`--no-input`)
Excludes code cells, shows only outputs and markdown.  
**Use case:** Reports for non-technical audiences.

### No Prompt (`--no-prompt`)
Removes `In[1]:` and `Out[1]:` prompts.  
**Use case:** Clean documentation or presentations.

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | All exports successful |
| 1 | File not found or invalid notebook |
| 2 | No valid formats specified |
| 3 | One or more exports failed (partial success) |

## Notes

- **Multiple formats:** Can export to multiple formats in one command
- **Preserves structure:** Maintains notebook cell order and structure
- **Image handling:** Images are embedded in HTML/PDF, extracted for Markdown
- **Python export:** Converts to .py with markdown as comments
- **Slides format:** Creates reveal.js presentation (HTML-based)

## Common Format Combinations

| Use Case | Formats | Command |
|----------|---------|---------|
| Reports | HTML, PDF | `-f html,pdf` |
| Documentation | Markdown, HTML | `-f md,html` |
| Code extraction | Python | `-f py` |
| Complete archive | All formats | `-f html,pdf,md,py` |
| Presentations | Slides, PDF | `-f slides,pdf` |

## Related Commands

- [`extract`](extract.md) - Extract outputs (images, data) separately
- [`run`](run.md) - Execute notebooks before exporting
- [`clean`](clean.md) - Clean notebooks before exporting

## See Also

- [Examples](../examples/export.md) - Practical usage examples
- [Getting Started](../getting-started/welcome.md) - Introduction to nbutils

