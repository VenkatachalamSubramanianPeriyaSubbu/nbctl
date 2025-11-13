# Getting Help with nbctl

Need help with nbctl? You're in the right place! Here's how to get assistance.

## Documentation

### Command-Line Help

The fastest way to get help is using the built-in help system:

```bash
# General help
nbctl --help

# Help for a specific command
nbctl clean --help
nbctl info --help
nbctl security --help

# Get version information
nbctl --version
```

Every command has detailed help with:
- Command description
- Available options
- Usage examples
- Default values

### Online Documentation

You're reading it! Our documentation covers:

- **[Getting Started](welcome.md)** - Introduction and overview
- **[Installation Guide](installation.md)** - How to install and set up
- **[CLI Reference](../cli/clean.md)** - Complete command documentation
- **[Examples](../examples/clean.md)** - Practical use cases and tutorials
- **[Version Policy](version-policy.md)** - Versioning and compatibility

---

## Found a Bug?

If you encounter a bug or unexpected behavior:

### 1. Check Existing Issues
Search our [GitHub Issues](https://github.com/VenkatachalamSubramanianPeriyaSubbu/nbctl/issues) to see if it's already reported.

### 2. Create a New Issue
If it's a new bug, [open an issue](https://github.com/VenkatachalamSubramanianPeriyaSubbu/nbctl/issues/new) with:

**Required Information:**
- nbctl version (`nbctl --version`)
- Python version (`python --version`)
- Operating system (macOS, Linux, Windows)
- Command you ran
- Error message (full traceback if available)
- Expected vs actual behavior

**Example:**
```markdown
**nbctl version:** 0.1.2
**Python version:** 3.9.7
**OS:** macOS 12.3

**Command:**
nbctl clean notebook.ipynb

**Error:**
ValueError: Invalid notebook format

**Expected:** Notebook should be cleaned
**Actual:** Command failed with error
```

### 3. Minimal Reproducible Example
If possible, provide:
- A minimal notebook that reproduces the issue
- Exact commands to reproduce
- Any relevant configuration files

---

## Feature Requests

Have an idea for a new feature or improvement?

### 1. Check the Roadmap
Review our [project README](https://github.com/VenkatachalamSubramanianPeriyaSubbu/nbctl#roadmap) to see planned features.

### 2. Submit a Feature Request
[Open an issue](https://github.com/VenkatachalamSubramanianPeriyaSubbu/nbctl/issues/new) with the label "enhancement":

**Include:**
- Clear description of the feature
- Use case: Why is this useful?
- Proposed implementation (if you have ideas)
- Examples of how it would work

**Example:**
```markdown
**Feature:** Add support for exporting to Word documents

**Use Case:** 
Many data scientists need to share analyses with stakeholders 
who prefer Word documents over PDFs or HTML.

**Proposed Usage:**
nbctl export notebook.ipynb -f docx

**Benefits:**
- Easier sharing with non-technical stakeholders
- Better integration with Word-based workflows
```

---

## Questions & Discussion

### General Questions

For general questions about nbctl:

1. **Check the docs** - Most questions are answered in the [CLI Reference](../cli/clean.md) or [Examples](../examples/clean.md)
2. **GitHub Discussions** - Start a discussion in our GitHub repository
3. **Stack Overflow** - Tag questions with `nbctl` and `jupyter-notebook`

### Common Questions

**Q: How do I install nbctl?**  
A: See our [Installation Guide](installation.md)

**Q: Which command should I use for X?**  
A: Check the [CLI Reference](../cli/clean.md) for a complete list

**Q: Can I use nbctl in CI/CD?**  
A: Yes! See the [Run command](../cli/run.md) and [Security command](../cli/security.md)

**Q: How do I contribute?**  
A: See the [Contributing](#contributing) section below

---

## Contributing

Want to contribute to nbctl? We'd love your help!

### Ways to Contribute

1. **Report Bugs** - Help us improve by reporting issues
2. **Suggest Features** - Share your ideas for new features
3. **Fix Bugs** - Submit pull requests for known issues
4. **Add Features** - Implement new functionality
5. **Improve Docs** - Fix typos, clarify explanations, add examples
6. **Write Tests** - Increase test coverage

### Getting Started with Development

```bash
# 1. Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/nbctl.git
cd nbctl

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install in development mode
pip install -e ".[dev]"

# 4. Run tests
pytest tests/ -v

# 5. Make your changes

# 6. Run tests again
pytest tests/ -v

# 7. Format code
black nbctl/ tests/

# 8. Submit a pull request
```

### Pull Request Guidelines

- **One feature per PR** - Keep PRs focused
- **Add tests** - New features need test coverage
- **Update docs** - Document new features/changes
- **Follow style** - Use black for formatting
- **Write good commit messages** - Clear and descriptive

---

## Troubleshooting

### Common Issues

#### Installation Problems

**Issue:** `pip install nbctl` fails

**Solutions:**
```bash
# Upgrade pip
pip install --upgrade pip

# Install with user flag
pip install --user nbctl

# Use virtual environment
python -m venv venv
source venv/bin/activate
pip install nbctl
```

---

#### Command Not Found

**Issue:** `nbctl: command not found`

**Solutions:**
```bash
# Check if installed
pip list | grep nbctl

# Check Python path
echo $PATH

# Try running with python -m
python -m nbctl.cli --help

# Reinstall
pip uninstall nbctl
pip install nbctl
```

---

#### Permission Errors

**Issue:** Permission denied when cleaning notebooks

**Solutions:**
```bash
# Check file permissions
ls -la notebook.ipynb

# Use output flag to write to a different location
nbctl clean notebook.ipynb -o output.ipynb

# Check if file is open in Jupyter
# Close the notebook in Jupyter and try again
```

---

#### Module Import Errors

**Issue:** `ModuleNotFoundError: No module named 'nbformat'`

**Solution:**
```bash
# Reinstall dependencies
pip install -r requirements.txt

# Or reinstall nbctl
pip uninstall nbctl
pip install nbctl
```

---

#### PDF Export Fails

**Issue:** PDF export doesn't work

**Solution:**
```bash
# PDF export requires LaTeX
# On macOS:
brew install --cask mactex

# On Ubuntu/Debian:
sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-plain-generic

# On Windows:
# Download and install MiKTeX from https://miktex.org/
```

---

## Contact

### Project Maintainer

- **Name:** Venkatachalam Subramanian Periya Subbu
- **GitHub:** [@VenkatachalamSubramanianPeriyaSubbu](https://github.com/VenkatachalamSubramanianPeriyaSubbu)
- **Email:** venkatachalam.sps@gmail.com

### Project Links

- **Repository:** [github.com/VenkatachalamSubramanianPeriyaSubbu/nbctl](https://github.com/VenkatachalamSubramanianPeriyaSubbu/nbctl)
- **Issues:** [github.com/VenkatachalamSubramanianPeriyaSubbu/nbctl/issues](https://github.com/VenkatachalamSubramanianPeriyaSubbu/nbctl/issues)
- **Documentation:** You're reading it!

---

## Community

### Stay Updated

- **Star** the repository to stay updated
- **Watch** for new releases
- **Subscribe** to issues for discussions

### Share Your Experience

- Write blog posts about nbctl
- Share on social media
- Present at meetups or conferences
- Create tutorials and examples

---

## Quick Links

- [Installation Guide](installation.md)
- [CLI Reference](../cli/clean.md)
- [Examples](../examples/clean.md)
- [GitHub Issues](https://github.com/VenkatachalamSubramanianPeriyaSubbu/nbctl/issues)
- [GitHub Repository](https://github.com/VenkatachalamSubramanianPeriyaSubbu/nbctl)

---

**Still need help? Don't hesitate to open an issue or start a discussion!**

