# nbutils 🚀

**The Swiss Army Knife for Jupyter Notebooks**

A comprehensive, production-ready CLI toolkit for Jupyter notebooks that solves all major pain points: version control, collaboration, code quality, security, and workflow automation.

[![Tests](https://img.shields.io/badge/tests-111%20passing-brightgreen)]()
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)]()
[![License](https://img.shields.io/badge/license-MIT-blue)]()

## ✨ Features

- 🧹 **Clean** - Remove outputs and metadata for git
- 📊 **Info** - Analyze notebook statistics and dependencies
- 📤 **Export** - Convert to HTML, PDF, Markdown, Python, etc.
- ✅ **Lint** - Check code quality and best practices
- 🎨 **Format** - Auto-format with black
- 🔧 **Git Setup** - Configure git for notebooks
- 🔍 **Diff** - Compare notebooks intelligently
- 📎 **Combine** - Concatenate notebooks
- 🔀 **Resolve** - 3-way merge with conflict detection (powered by nbdime)
- 🔒 **Security** - Find security vulnerabilities

## 📦 Installation

```bash
pip install -e .
```

Or install from source:

```bash
git clone https://github.com/yourusername/nbutils.git
cd nbutils
pip install -e .
```

## 🚀 Quick Start

### Clean notebooks for git

```bash
nbutils clean notebook.ipynb
```

**Removes:** Outputs, execution counts, metadata  
**Result:** Smaller files, cleaner diffs, fewer conflicts ✨

### Get notebook insights

```bash
nbutils info notebook.ipynb
```

**Shows:** Statistics, code metrics, dependencies, imports

### Scan for security issues

```bash
nbutils security notebook.ipynb
```

**Detects:** Hardcoded secrets, SQL injection, unsafe pickle, and more 🔒

### Compare notebooks

```bash
nbutils diff notebook1.ipynb notebook2.ipynb
```

**Compares:** Only source code (ignores outputs/metadata)

### Resolve merge conflicts

```bash
nbutils resolve base.ipynb ours.ipynb theirs.ipynb -o merged.ipynb
```

**Uses:** nbdime's intelligent 3-way merge with conflict detection

## 📚 Commands Reference

### 🧹 `nbutils clean`

Remove outputs and metadata from notebooks for version control.

```bash
nbutils clean notebook.ipynb [OPTIONS]
```

**Options:**
- `--output, -o PATH` - Save to different file
- `--keep-outputs` - Preserve cell outputs
- `--keep-execution-count` - Preserve execution counts
- `--keep-metadata` - Preserve metadata
- `--dry-run` - Preview changes without modifying

**Examples:**
```bash
# Clean in place
nbutils clean notebook.ipynb

# Preview changes
nbutils clean notebook.ipynb --dry-run

# Save to new file
nbutils clean notebook.ipynb -o clean.ipynb
```

---

### 📊 `nbutils info`

Display comprehensive notebook statistics and analysis.

```bash
nbutils info notebook.ipynb [OPTIONS]
```

**Options:**
- `--code-metrics` - Show only code metrics
- `--imports` - Show only import statements

**Shows:**
- Cell counts (code, markdown, raw)
- File size
- Code metrics (lines, complexity, empty cells)
- All import statements and dependencies

**Examples:**
```bash
# Full analysis
nbutils info notebook.ipynb

# Just imports
nbutils info notebook.ipynb --imports
```

---

### 📤 `nbutils export`

Convert notebooks to multiple formats simultaneously.

```bash
nbutils export notebook.ipynb --format FORMATS [OPTIONS]
```

**Supported Formats:**
- `html` - HTML document
- `pdf` - PDF (requires LaTeX)
- `markdown`, `md` - Markdown
- `python`, `py` - Python script
- `latex`, `tex` - LaTeX
- `rst` - reStructuredText
- `slides` - Reveal.js presentations

**Options:**
- `--format, -f` - Output formats (comma-separated, required)
- `--output-dir, -o` - Output directory
- `--no-input` - Exclude input cells
- `--no-prompt` - Exclude prompts

**Examples:**
```bash
# Export to multiple formats
nbutils export notebook.ipynb -f html,pdf,py

# Export without input cells
nbutils export notebook.ipynb -f html --no-input

# Export presentation
nbutils export notebook.ipynb -f slides
```

---

### ✅ `nbutils lint`

Check code quality and identify issues.

```bash
nbutils lint notebook.ipynb [OPTIONS]
```

**Checks:**
- ❌ Unused imports
- 📏 Overly long cells
- 🔲 Empty code cells
- 🐛 Code quality issues

**Options:**
- `--max-cell-length INT` - Max lines per cell (default: 100)

**Examples:**
```bash
# Standard linting
nbutils lint notebook.ipynb

# Custom cell length limit
nbutils lint notebook.ipynb --max-cell-length 150
```

---

### 🎨 `nbutils format`

Auto-format code cells with black.

```bash
nbutils format notebook.ipynb [OPTIONS]
```

**Options:**
- `--output-dir, -o` - Output directory
- `--line-length INT` - Max line length (default: 88)

**Examples:**
```bash
# Format in place
nbutils format notebook.ipynb

# Custom line length
nbutils format notebook.ipynb --line-length 100
```

---

### 🔧 `nbutils git-setup`

Configure git for optimal notebook workflows.

```bash
nbutils git-setup
```

**Configures:**
- ✅ `.gitattributes` for notebook handling
- ✅ `.gitignore` for Python projects
- ✅ Custom diff driver using nbutils
- ✅ Custom merge driver using nbutils

**Run once per repository to enable git integration.**

---

### 🔍 `nbutils diff`

Compare notebooks intelligently (ignores outputs and metadata).

```bash
nbutils diff notebook1.ipynb notebook2.ipynb [OPTIONS]
```

**Options:**
- `--format, -f` - Output format: `table`, `unified`, `json` (default: table)
- `--code-only` - Show only code cell changes
- `--stats` - Show only statistics

**Features:**
- ✅ Ignores outputs and metadata
- ✅ Focuses on actual code changes
- ✅ Multiple output formats

**Examples:**
```bash
# Table view (default)
nbutils diff old.ipynb new.ipynb

# Unified diff format
nbutils diff old.ipynb new.ipynb --format unified

# Show only code changes
nbutils diff old.ipynb new.ipynb --code-only

# JSON output for automation
nbutils diff old.ipynb new.ipynb --format json
```

---

### 📎 `nbutils combine`

Concatenate or combine two notebooks.

```bash
nbutils combine notebook1.ipynb notebook2.ipynb -o output.ipynb [OPTIONS]
```

**Strategies:**
- `append` - Concatenate all cells from both (default)
- `first` - Keep only first notebook
- `second` - Keep only second notebook

**Options:**
- `--output, -o` - Output file (required)
- `--strategy` - Combine strategy
- `--report` - Show detailed report

**Examples:**
```bash
# Concatenate notebooks
nbutils combine analysis1.ipynb analysis2.ipynb -o full.ipynb

# Keep only first notebook (copy)
nbutils combine nb1.ipynb nb2.ipynb -o output.ipynb --strategy first
```

**Note:** For true merging with conflict detection, use `nbutils resolve`.

---

### 🔀 `nbutils resolve`

Intelligent 3-way merge with conflict detection (powered by nbdime).

```bash
nbutils resolve base.ipynb ours.ipynb theirs.ipynb -o merged.ipynb [OPTIONS]
```

**Arguments:**
- `BASE` - Common ancestor (before changes)
- `OURS` - Your version (local changes)
- `THEIRS` - Other version (remote changes)

**Options:**
- `--output, -o` - Output file (required unless --check-conflicts)
- `--strategy` - Merge strategy: `auto`, `ours`, `theirs`, `cell-append`
- `--check-conflicts` - Check for conflicts only (no output file needed)
- `--report` - Show detailed merge report

**Features:**
- ✅ Production-grade merging with nbdime
- ✅ Automatic conflict detection
- ✅ Conflict markers for manual resolution
- ✅ Multiple merge strategies

**Examples:**
```bash
# Check for conflicts first
nbutils resolve base.ipynb ours.ipynb theirs.ipynb --check-conflicts

# Perform merge
nbutils resolve base.ipynb ours.ipynb theirs.ipynb -o merged.ipynb

# Use with Git
git show :1:notebook.ipynb > base.ipynb
git show :2:notebook.ipynb > ours.ipynb
git show :3:notebook.ipynb > theirs.ipynb
nbutils resolve base.ipynb ours.ipynb theirs.ipynb -o notebook.ipynb
```

---

### 🔒 `nbutils security`

Scan notebooks for security vulnerabilities.

```bash
nbutils security notebook.ipynb [OPTIONS]
```

**Detects:**
- 🔴 **HIGH**: Hardcoded secrets (API keys, passwords, tokens)
- 🔴 **HIGH**: Unsafe pickle deserialization
- 🔴 **HIGH**: SQL injection risks
- 🟡 **MEDIUM**: Command injection (os.system, eval, exec)
- 🟡 **MEDIUM**: Unsafe YAML parsing
- 🟡 **MEDIUM**: Disabled SSL verification
- 🔵 **LOW**: Weak cryptographic algorithms (MD5, SHA1)

**Options:**
- `--severity` - Filter by severity: `low`, `medium`, `high`, `all` (default: all)
- `--json` - Output as JSON
- `--verbose, -v` - Show detailed recommendations

**Examples:**
```bash
# Scan for all issues
nbutils security notebook.ipynb

# Only high severity
nbutils security notebook.ipynb --severity high

# With recommendations
nbutils security notebook.ipynb --verbose

# JSON output for CI/CD
nbutils security notebook.ipynb --json
```

---

## 🎯 Common Workflows

### Setting up a new repository

```bash
# 1. Configure git for notebooks
nbutils git-setup

# 2. Clean notebooks before committing
nbutils clean *.ipynb

# 3. Check code quality
nbutils lint notebook.ipynb
nbutils format notebook.ipynb

# 4. Scan for security issues
nbutils security notebook.ipynb
```

### Reviewing notebook changes

```bash
# Compare versions
nbutils diff old.ipynb new.ipynb --format unified

# Check what changed (code only)
nbutils diff old.ipynb new.ipynb --code-only
```

### Resolving merge conflicts

```bash
# Check if there are conflicts
nbutils resolve base.ipynb ours.ipynb theirs.ipynb --check-conflicts

# Perform merge
nbutils resolve base.ipynb ours.ipynb theirs.ipynb -o merged.ipynb --report

# If conflicts exist, manually resolve in the merged file
```

### Pre-commit checks

```bash
# Quality checks
nbutils lint notebook.ipynb
nbutils format notebook.ipynb
nbutils security notebook.ipynb --severity high

# Clean for commit
nbutils clean notebook.ipynb
```

---

## 🔧 Development

### Setup

```bash
# Clone repository
git clone https://github.com/yourusername/nbutils.git
cd nbutils

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"
```

### Run Tests

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_security.py -v

# With coverage
pytest tests/ --cov=nbutils --cov-report=html
```

### Code Quality

```bash
# Format code
black nbutils/ tests/

# Type checking
mypy nbutils/
```

---

## 📊 Test Coverage

```
111 tests passing
✅ Clean command (5 tests)
✅ Combine command (10 tests)
✅ Diff command (18 tests)
✅ Export command (7 tests)
✅ Format command (6 tests)
✅ Git setup command (14 tests)
✅ Info command (6 tests)
✅ Lint command (6 tests)
✅ Resolve command (20 tests)
✅ Security command (19 tests)
```

---

## 🤝 Why nbutils?

Jupyter notebooks are powerful but have challenges:

| Problem | nbutils Solution |
|---------|------------------|
| ❌ Massive git diffs | ✅ `clean` - Remove outputs |
| ❌ Merge conflicts | ✅ `resolve` - Intelligent 3-way merge |
| ❌ Hard to compare | ✅ `diff` - Smart comparison |
| ❌ Code quality issues | ✅ `lint` + `format` |
| ❌ Security risks | ✅ `security` - Vulnerability scanning |
| ❌ Manual workflows | ✅ Comprehensive CLI automation |

**One tool. All solutions. Production-ready.** 🚀

---

## 🗺️ Roadmap

- [x] Basic clean command
- [x] Info command (statistics, metrics, imports)
- [x] Export command (HTML, PDF, Markdown, etc.)
- [x] Lint command (code quality)
- [x] Format command (black auto-format)
- [x] Git setup (integration)
- [x] Diff command (intelligent comparison)
- [x] Combine command (2-way merge)
- [x] Resolve command (3-way merge with nbdime)
- [x] Security command (vulnerability scanning)
- [ ] Test runner (execute and validate)
- [ ] Split command (break large notebooks)
- [ ] Template system
- [ ] Cloud integration

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Built with ❤️ for the Jupyter community by [Venkatachalam Subramanian Periya Subbu](https://github.com/yourusername)

---

## 🌟 Status

**Version:** 0.1.0  
**Status:** Production-ready with comprehensive test coverage  
**Tests:** 111 passing ✅

---

**⭐ Star this repo if you find it useful!**
