# nbutils

**The Swiss Army Knife for Jupyter Notebooks**

A comprehensive CLI toolkit for working with Jupyter notebooks in version control, collaboration, and production workflows.

## Installation

```bash
pip install -e .
```

## Quick Start

### Clean a notebook for git

```bash
nbutils clean notebook.ipynb
```

This removes:
- Cell outputs
- Execution counts  
- Unnecessary metadata

**Result:** Smaller files, cleaner git diffs, no merge conflicts!

### Options

```bash
# Save to a different file
nbutils clean notebook.ipynb --output clean.ipynb

# Keep outputs
nbutils clean notebook.ipynb --keep-outputs

# Dry run (see what would be changed)
nbutils clean notebook.ipynb --dry-run
```

### Get notebook information

```bash
nbutils info notebook.ipynb
```

This shows:
- Total cells (code, markdown, raw)
- File size
- Code metrics (total lines, average lines per cell, largest/smallest cells, empty cells)
- All import statements used in the notebook

**Perfect for:** Understanding dependencies, checking notebook complexity, auditing libraries used.

### Export to multiple formats

```bash
nbutils export notebook.ipynb --format html,pdf,py
```

This exports to:
- HTML documents
- PDF files (requires LaTeX)
- Python scripts
- Markdown, LaTeX, reStructuredText, and more!

**Perfect for:** Sharing notebooks, creating documentation, converting to production code.

## Commands

### `nbutils clean`
Remove outputs and metadata from notebooks to prepare them for version control.

**Usage:**
```bash
nbutils clean notebook.ipynb [OPTIONS]
```

**Options:**
- `--output, -o PATH` - Save to a different file (default: overwrites input)
- `--keep-outputs` - Keep cell outputs
- `--keep-execution-count` - Keep execution counts
- `--keep-metadata` - Keep all metadata
- `--dry-run` - Show what would be cleaned without making changes

**Examples:**
```bash
# Clean in place
nbutils clean notebook.ipynb

# Save to new file
nbutils clean notebook.ipynb -o clean.ipynb

# Preview changes
nbutils clean notebook.ipynb --dry-run
```

### `nbutils info`
Display statistics, code metrics, and import statements from a notebook.

**Usage:**
```bash
nbutils info notebook.ipynb [OPTIONS]
```

**Options:**
- `--code-metrics` - Show only code metrics
- `--imports` - Show only imports

**Shows (by default, shows all):**
- Cell counts (total, code, markdown, raw)
- File size
- Code metrics:
  - Total lines of code
  - Average lines per cell
  - Largest and smallest cells
  - Empty code cells count
- All import statements found in code cells

**Examples:**
```bash
# Show all information
nbutils info notebook.ipynb

# Show only code metrics
nbutils info notebook.ipynb --code-metrics

# Show only imports
nbutils info notebook.ipynb --imports
```

### `nbutils export`
Export notebooks to multiple formats at once using nbconvert.

**Usage:**
```bash
nbutils export notebook.ipynb --format FORMATS [OPTIONS]
```

**Options:**
- `--format, -f FORMATS` - Output formats (comma-separated, required)
- `--output-dir, -o PATH` - Output directory (default: same as notebook)
- `--no-input` - Exclude input cells from output
- `--no-prompt` - Exclude input/output prompts

**Supported Formats:**
- `html` - HTML document
- `pdf` - PDF document (requires LaTeX or webpdf)
- `markdown` or `md` - Markdown file
- `python` or `py` - Python script
- `latex` or `tex` - LaTeX document
- `rst` - reStructuredText
- `slides` - Reveal.js slides (HTML)

**Examples:**
```bash
# Export to multiple formats
nbutils export notebook.ipynb -f html,pdf,py

# Export to specific directory
nbutils export notebook.ipynb -f html --output-dir exports/

# Export without input cells (output only)
nbutils export notebook.ipynb -f html --no-input

# Export presentation slides
nbutils export notebook.ipynb -f slides
```

## Coming Soon

- **`nbutils diff`** - Smart notebook comparison
- **`nbutils merge`** - Intelligent 3-way merge
- And many more!

## Development

### Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"
```

### Run Tests

```bash
pytest tests/ -v
```

### Format Code

```bash
black nbutils/ tests/
```

## Why nbutils?

Jupyter notebooks are amazing for data science and research, but they have pain points:

- Don't work well with git (massive diffs, merge conflicts)
- Hard to collaborate on
- Quality assurance is manual
- Converting to production code is painful

**nbutils solves all of these problems in one unified CLI.**

## Roadmap

- [x] Basic clean command
- [x] Info command (statistics, code metrics, and imports)
- [x] Export command (convert to HTML, PDF, Markdown, Python, etc.)
- [ ] Diff and merge tools
- [ ] Quality tools (lint, test, format)
- [ ] Productivity tools (split, templates)
- [ ] Git integration
- [ ] Cloud features

## Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details.

## Author

Built with love for the Jupyter community

---

**Status:** Early development (v0.1.0)