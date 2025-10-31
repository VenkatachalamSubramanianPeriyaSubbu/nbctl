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
- ✓ Cell outputs
- ✓ Execution counts  
- ✓ Unnecessary metadata

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

## Features

### Currently Available

- **`nbutils clean`** - Remove outputs and metadata for version control

### Coming Soon

- **`nbutils diff`** - Smart notebook comparison
- **`nbutils merge`** - Intelligent 3-way merge
- **`nbutils info`** - Notebook statistics
- **`nbutils export`** - Multi-format export
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

- ❌ Don't work well with git (massive diffs, merge conflicts)
- ❌ Hard to collaborate on
- ❌ Quality assurance is manual
- ❌ Converting to production code is painful

**nbutils solves all of these problems in one unified CLI.**

## Roadmap

- [x] Basic clean command
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

Built with ❤️ for the Jupyter community

---

**Status:** Early development (v0.1.0)