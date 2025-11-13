# Installation

Get nbctl up and running in minutes!

## Requirements

- **Python:** 3.8 or higher
- **Operating Systems:** macOS, Linux, Windows
- **Jupyter:** Required (for working with notebooks)

## Quick Install

### Using pip (Recommended)

```bash
pip install nbctl
```

### Verify Installation

```bash
# Check version
nbctl --version

# Show help
nbctl --help
```

---

## Installation Methods

### 1. Install from PyPI (Recommended)

For most users, installing from PyPI is the easiest option:

```bash
# Basic installation
pip install nbctl

# With development tools
pip install nbctl[dev]
```

---

### 2. Install from Source (Development)

For contributors or users who want the latest development version:

```bash
# Clone the repository
git clone https://github.com/VenkatachalamSubramanianPeriyaSubbu/nbutils.git
cd nbutils

# Install in editable mode
pip install -e .

# Or with development dependencies
pip install -e ".[dev]"
```

**Benefits:**
- Get the latest features
- Make local modifications
- Contribute to development

---

### 3. Install in Virtual Environment (Recommended)

Using a virtual environment keeps your system Python clean:

```bash
# Create virtual environment
python -m venv nbutils-env

# Activate on macOS/Linux
source nbutils-env/bin/activate

# Activate on Windows
nbutils-env\Scripts\activate

# Install nbutils
pip install nbctl

# Deactivate when done
deactivate
```

---

### 4. Install with pip User Flag

If you don't have admin privileges:

```bash
pip install --user nbutils
```

The command will be installed in your user directory.

---

## Dependencies

nbctl automatically installs these dependencies:

### Core Dependencies
- **nbformat** (≥5.0.0) - Notebook file format
- **click** (≥8.0.0) - CLI framework
- **rich** (≥13.0.0) - Terminal formatting
- **nbconvert** (≥7.0.0) - Notebook conversion
- **nbclient** (≥0.7.0) - Notebook execution
- **nbdime** (≥3.0.0) - Notebook diffing and merging

### Development Dependencies (Optional)
- **pytest** (≥7.0.0) - Testing framework
- **pytest-cov** (≥4.0.0) - Test coverage
- **black** (≥23.0.0) - Code formatting
- **mypy** (≥1.0.0) - Type checking

To install with development dependencies:

```bash
pip install nbctl[dev]
```

---

## Optional Dependencies

### For PDF Export

PDF export requires LaTeX to be installed on your system:

#### macOS
```bash
brew install --cask mactex
```

#### Ubuntu/Debian
```bash
sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-plain-generic
```

#### Windows
Download and install [MiKTeX](https://miktex.org/)

#### Verify LaTeX
```bash
pdflatex --version
```

---

## Post-Installation Setup

### Configure Git Integration (Optional)

For optimal notebook version control, set up git integration:

```bash
# Run in your git repository
cd your-repo
nbctl git-setup
```

This configures:
- `.gitattributes` for notebook handling
- `.gitignore` for Python projects
- Custom diff driver using nbutils
- Custom merge driver using nbutils

---

### Verify Everything Works

Test nbctl with a sample notebook:

```bash
# Create a test notebook (if you have Jupyter)
jupyter notebook

# Or test with an existing notebook
nbctl info your-notebook.ipynb

# Clean a notebook
nbctl clean your-notebook.ipynb --dry-run

# Get statistics
nbctl info your-notebook.ipynb
```

---

## Upgrading

### Upgrade to Latest Version

```bash
# Upgrade from PyPI
pip install --upgrade nbutils

# Check new version
nbctl --version
```

### Upgrade from Development Branch

```bash
cd nbutils
git pull origin main
pip install -e .
```

---

## Uninstalling

If you need to uninstall nbutils:

```bash
pip uninstall nbutils
```

To also remove dependencies (if not used by other packages):

```bash
pip uninstall nbctl nbformat click rich nbconvert nbclient nbdime
```

---

## Troubleshooting

### Command Not Found

**Problem:** `nbutils: command not found` after installation

**Solutions:**

1. **Check if installed:**
   ```bash
   pip list | grep nbutils
   ```

2. **Check Python path:**
   ```bash
   echo $PATH
   python -m site --user-base
   ```

3. **Run with python -m:**
   ```bash
   python -m nbutils.cli --help
   ```

4. **Add to PATH (macOS/Linux):**
   ```bash
   export PATH="$HOME/.local/bin:$PATH"
   # Add to ~/.bashrc or ~/.zshrc to make permanent
   ```

---

### Permission Errors

**Problem:** Permission denied during installation

**Solutions:**

1. **Use virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install nbctl
   ```

2. **Use --user flag:**
   ```bash
   pip install --user nbutils
   ```

3. **Use sudo** (not recommended):
   ```bash
   sudo pip install nbctl
   ```

---

### Import Errors

**Problem:** `ModuleNotFoundError` when running nbutils

**Solutions:**

1. **Reinstall dependencies:**
   ```bash
   pip install --force-reinstall nbutils
   ```

2. **Check Python version:**
   ```bash
   python --version  # Should be 3.8 or higher
   ```

3. **Use explicit Python:**
   ```bash
   python3 -m pip install nbctl
   python3 -m nbutils.cli --help
   ```

---

### Installation Fails

**Problem:** `pip install nbctl` fails with errors

**Solutions:**

1. **Upgrade pip:**
   ```bash
   pip install --upgrade pip setuptools wheel
   ```

2. **Clear pip cache:**
   ```bash
   pip cache purge
   pip install nbctl
   ```

3. **Install from source:**
   ```bash
   git clone https://github.com/VenkatachalamSubramanianPeriyaSubbu/nbutils.git
   cd nbutils
   pip install -e .
   ```

---

## Platform-Specific Notes

### macOS

- **Recommended:** Use [Homebrew](https://brew.sh/) to manage Python
- **M1/M2 Macs:** No special configuration needed
- **Python 2 vs 3:** Use `python3` and `pip3` explicitly

```bash
# Install Python via Homebrew
brew install python3

# Install nbutils
pip3 install nbutils
```

---

### Linux

- **Ubuntu/Debian:**
  ```bash
  sudo apt-get update
  sudo apt-get install python3-pip
  pip3 install nbutils
  ```

- **Fedora/CentOS:**
  ```bash
  sudo dnf install python3-pip
  pip3 install nbutils
  ```

- **Arch:**
  ```bash
  sudo pacman -S python-pip
  pip install nbctl
  ```

---

### Windows

- **Recommended:** Use [Python from python.org](https://www.python.org/downloads/)
- **Add Python to PATH** during installation
- **Use Command Prompt or PowerShell**

```powershell
# Install nbutils
pip install nbctl

# If command not found, try:
python -m pip install nbctl
python -m nbutils.cli --help
```

---

## Docker Installation (Advanced)

For containerized environments:

```dockerfile
FROM python:3.9-slim

# Install nbutils
RUN pip install nbctl

# Verify installation
RUN nbctl --version

# Set working directory
WORKDIR /notebooks

# Default command
CMD ["nbutils", "--help"]
```

Build and run:

```bash
docker build -t nbctl .
docker run -v $(pwd):/notebooks nbctl clean notebook.ipynb
```

---

## Next Steps

Now that you have nbctl installed:

1. **[Learn the basics](welcome.md)** - Understand what nbctl can do
2. **[Explore commands](../cli/clean.md)** - See all available commands
3. **[Try examples](../examples/clean.md)** - Hands-on learning
4. **[Configure git](../cli/git-setup.md)** - Set up version control

---

## Getting Help

Need help with installation?

- Check the [Help Guide](help.md)
- [Open an issue](https://github.com/VenkatachalamSubramanianPeriyaSubbu/nbutils/issues)
- Search [existing issues](https://github.com/VenkatachalamSubramanianPeriyaSubbu/nbutils/issues?q=is%3Aissue)

---

**Installation complete! Ready to use nbutils? Check out the [examples](../examples/clean.md)!**

