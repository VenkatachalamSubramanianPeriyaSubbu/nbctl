# nbctl git-setup

Configure git for optimal notebook workflows.

## Description

The `git-setup` command automatically configures your git repository for optimal Jupyter notebook handling. It sets up custom diff and merge drivers, creates appropriate `.gitattributes` and `.gitignore` files, and enables intelligent notebook version control.

**Run once per repository** to enable git integration for all notebooks.

Use this command to:
- Enable intelligent notebook diffs in git
- Set up automatic merge resolution
- Configure proper .gitignore for Python projects
- Make notebooks git-friendly
- Improve collaboration workflow

## Usage

```bash
nbctl git-setup
```

## Arguments

None. Command operates on current git repository.

## Options

None. Uses sensible defaults for all configurations.

## What It Configures

### 1. `.gitattributes` File

Created/updated with notebook-specific rules:

```
*.ipynb diff=nbctl
*.ipynb merge=nbctl
```

This tells git to use nbctl for diffing and merging notebooks.

---

### 2. `.gitignore` File

Created/updated with Python project patterns:

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/
env.bak/
venv.bak/

# Jupyter
.ipynb_checkpoints/
*/.ipynb_checkpoints/*

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
```

---

### 3. Git Diff Driver

Registers nbctl as the diff driver for notebooks:

```bash
git config diff.nbctl.command 'nbctl diff'
```

**Result:** When you run `git diff notebook.ipynb`, git uses nbctl diff which:
- Ignores outputs and metadata
- Shows only source code changes
- Provides clean, readable diffs

---

### 4. Git Merge Driver

Registers nbctl as the merge driver for notebooks:

```bash
git config merge.nbctl.driver 'nbctl resolve %O %A %B -o %A'
```

**Result:** When notebooks have merge conflicts, git uses nbctl resolve which:
- Intelligently merges notebooks
- Detects real conflicts
- Provides clear conflict markers
- Preserves notebook structure

## Output

### Success

```
Git configuration completed successfully!

Created/Updated:
  - .gitattributes (notebook handling rules)
  - .gitignore (Python project patterns)

Configured:
  - Custom diff driver: nbctl diff
  - Custom merge driver: nbctl resolve

Your repository is now configured for optimal notebook workflows!

Next steps:
  1. Review .gitignore to ensure it meets your needs
  2. Commit the configuration files:
     git add .gitattributes .gitignore
     git commit -m "Configure git for notebooks"
```

### Already Configured

```
Git already configured for notebooks

Existing configuration:
  - .gitattributes ✓
  - .gitignore ✓
  - Diff driver ✓
  - Merge driver ✓

No changes needed.
```

### Not a Git Repository

```
Error: Not a git repository

This command must be run inside a git repository.

To initialize:
  git init
  nbctl git-setup
```

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success, git configured |
| 1 | Not a git repository |
| 2 | Permission error |

## Configuration Scope

The command configures:

### Repository-Level (Local)
- `.gitattributes` - Committed to repository
- `.gitignore` - Committed to repository (if not exists)
- Diff driver - Stored in `.git/config`
- Merge driver - Stored in `.git/config`

### What's Committed
- `.gitattributes` - Shared with team
- `.gitignore` - Shared with team (if created)
- Git config - Local to your repository

**Note:** Team members should also run `nbctl git-setup` to enable custom drivers.

## After Setup Workflow

### Daily Workflow

```bash
# 1. Make changes to notebook
# (edit in Jupyter)

# 2. Check what changed (uses nbctl diff)
git diff notebook.ipynb
# Shows only source code changes!

# 3. Stage and commit
git add notebook.ipynb
git commit -m "Add data analysis"

# 4. Pull changes (uses nbctl resolve for conflicts)
git pull
# Notebooks merge intelligently!
```

### Recommended Workflow

```bash
# Before committing
nbctl clean notebook.ipynb    # Remove outputs
nbctl format notebook.ipynb   # Format code
nbctl lint notebook.ipynb     # Check quality

git add notebook.ipynb
git commit -m "Add analysis"
```

## Customization

### Modify .gitignore

After setup, you can edit `.gitignore` to add project-specific patterns:

```bash
# Edit .gitignore
vim .gitignore

# Add custom patterns
data/*.csv
models/*.pkl
secrets.env
```

### Modify .gitattributes

Add custom rules for other file types:

```bash
# Edit .gitattributes
vim .gitattributes

# Add custom rules
*.ipynb diff=nbctl merge=nbctl
*.csv diff=csv
*.json diff=json
```

## Verifying Configuration

### Check .gitattributes

```bash
cat .gitattributes
```

Expected content:
```
*.ipynb diff=nbctl
*.ipynb merge=nbctl
```

### Check .gitignore

```bash
cat .gitignore
```

Should include Python and Jupyter patterns.

### Check Git Config

```bash
git config --list | grep nbctl
```

Expected output:
```
diff.nbctl.command=nbctl diff
merge.nbctl.driver=nbctl resolve %O %A %B -o %A
```

## Team Setup

### For Repository Owner

```bash
# 1. Run git-setup
nbctl git-setup

# 2. Commit configuration
git add .gitattributes .gitignore
git commit -m "Configure git for notebooks"
git push
```

### For Team Members

```bash
# 1. Pull changes
git pull

# 2. Run git-setup to enable custom drivers
nbctl git-setup
```

**Note:** `.gitattributes` and `.gitignore` are shared, but git config (drivers) are local.

## Troubleshooting

### Diff Still Shows JSON

**Problem:** `git diff` shows JSON instead of clean diff

**Solution:**
```bash
# Verify diff driver is configured
git config --list | grep diff.nbctl

# Re-run setup
nbctl git-setup

# Test
git diff notebook.ipynb
```

### Merge Conflicts Not Resolved

**Problem:** Notebook merge conflicts appear as JSON

**Solution:**
```bash
# Verify merge driver is configured
git config --list | grep merge.nbctl

# Re-run setup
nbctl git-setup

# Manual resolution
nbctl resolve base.ipynb ours.ipynb theirs.ipynb -o merged.ipynb
```

### Configuration Not Applied

**Problem:** Changes not taking effect

**Solution:**
```bash
# Check if in git repo
git status

# Check if .gitattributes exists
ls -la .gitattributes

# Force re-read of attributes
git rm --cached -r .
git reset --hard
```

## Notes

- **Run once:** Only needs to be run once per repository
- **Safe to re-run:** Running multiple times is safe (idempotent)
- **Team coordination:** Team members should also run it for full functionality
- **Repository-specific:** Settings are per-repository, not global
- **Preserves existing:** Won't overwrite custom .gitignore rules

## Related Commands

- [`clean`](clean.md) - Clean notebooks before committing
- [`diff`](diff.md) - Compare notebooks (used by git)
- [`resolve`](resolve.md) - Merge notebooks (used by git)
- [`format`](format.md) - Format notebooks before committing

## See Also

- [Examples](../examples/git-setup.md) - Practical usage examples
- [Getting Started](../getting-started/welcome.md) - Introduction to nbctl

