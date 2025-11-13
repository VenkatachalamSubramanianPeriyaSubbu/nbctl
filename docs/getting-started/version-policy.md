# Version Policy

Understanding nbctl versioning, compatibility, and update policies.

## Current Version

**nbctl 0.1.0** - Initial release

- **Status:** Stable
- **Python Support:** 3.8, 3.9, 3.10, 3.11, 3.12+
- **License:** MIT

---

## Semantic Versioning

nbctl follows [Semantic Versioning 2.0.0](https://semver.org/) (SemVer):

### Version Format: MAJOR.MINOR.PATCH

```
0.1.0
│ │ │
│ │ └─ PATCH: Bug fixes, minor improvements
│ └─── MINOR: New features, backward compatible
└───── MAJOR: Breaking changes, API changes
```

### What Each Number Means

#### MAJOR Version (X.0.0)
**Changed when:** Breaking changes that require user action

**Examples:**
- Removing or renaming commands
- Changing command-line interface
- Removing deprecated features
- Incompatible API changes

**Impact:** May require updating scripts and workflows

---

#### MINOR Version (0.X.0)
**Changed when:** New features added in a backward-compatible manner

**Examples:**
- Adding new commands
- Adding new options to existing commands
- Improving existing features
- New output formats

**Impact:** Safe to upgrade, new features available

---

#### PATCH Version (0.0.X)
**Changed when:** Bug fixes and minor improvements

**Examples:**
- Fixing bugs
- Performance improvements
- Documentation updates
- Dependency updates

**Impact:** Safe to upgrade, recommended for bug fixes

---

## Compatibility Guarantees

### Python Version Support

| nbctl Version | Python Versions | Status |
|----------------|-----------------|---------|
| 0.1.x | 3.8, 3.9, 3.10, 3.11, 3.12+ | Current |
| Future 1.x | 3.9+ (drop 3.8) | Planned |

**Policy:**
- Support for Python 3.8+ in 0.x series
- May drop older Python versions in major releases
- Minimum 6 months notice before dropping support

---

### Dependency Compatibility

nbctl depends on:

| Package | Minimum Version | Current Version |
|---------|----------------|-----------------|
| nbformat | 5.0.0 | Latest |
| click | 8.0.0 | Latest |
| rich | 13.0.0 | Latest |
| nbconvert | 7.0.0 | Latest |
| nbclient | 0.7.0 | Latest |
| nbdime | 3.0.0 | Latest |

**Policy:**
- Pin minimum versions, not maximum
- Test with latest versions regularly
- Update minimums in MINOR releases only

---

### Backward Compatibility

#### Command-Line Interface
- **0.x series:** Interface may change (alpha/beta)
- **1.x series:** Interface stable, changes in major versions only

#### Configuration Files
- **0.x series:** Format may change between minor versions
- **1.x series:** Format stable, migration guides provided

#### Output Formats
- **All versions:** May improve formatting without notice
- **Breaking changes:** Only in major versions

---

## Release Schedule

### Regular Releases

| Release Type | Frequency | Content |
|--------------|-----------|---------|
| **PATCH** | As needed | Bug fixes, critical fixes |
| **MINOR** | Monthly | New features, improvements |
| **MAJOR** | Yearly | Breaking changes, redesigns |

### Security Releases

- **Critical security fixes:** Released immediately
- **Minor security issues:** Bundled in next patch release
- **Security advisories:** Published on GitHub

---

## Deprecation Policy

### Deprecation Process

1. **Announcement** (Version N)
   - Feature marked as deprecated
   - Warning added to documentation
   - Alternative recommended

2. **Deprecation Period** (Version N+1)
   - Feature still works
   - Warning shown when used
   - Migration guide available

3. **Removal** (Version N+2, MAJOR only)
   - Feature removed
   - Clear error message if used

### Minimum Deprecation Period

- **MINOR features:** 2 minor versions (e.g., 0.1 → 0.3)
- **MAJOR features:** 1 major version (e.g., 1.0 → 2.0)
- **Critical features:** 1 year minimum

### Example Timeline

```
v0.1.0: Feature X introduced
v0.2.0: Feature Y introduced (better than X)
v0.3.0: Feature X deprecated, warning added
v0.4.0: Feature X still works with warning
v1.0.0: Feature X removed (major version)
```

---

## Update Recommendations

### How to Update

```bash
# Check current version
nbctl --version

# Update to latest version
pip install --upgrade nbctl

# Update to specific version
pip install nbctl==0.2.0
```

---

### Update Guidelines

#### PATCH Updates (0.0.X)
**Update immediately** - Bug fixes and improvements

```bash
pip install --upgrade nbctl
```

**Risk:** Minimal  
**Testing:** Not required  
**Rollback:** Easy if needed

---

#### MINOR Updates (0.X.0)
**Update regularly** - New features, backward compatible

```bash
# Review release notes first
pip install --upgrade nbctl
```

**Risk:** Low  
**Testing:** Basic smoke testing recommended  
**Rollback:** Easy if needed

---

#### MAJOR Updates (X.0.0)
**Review carefully** - May have breaking changes

```bash
# Read upgrade guide first
# Test in non-production environment
pip install --upgrade nbctl
```

**Risk:** Medium  
**Testing:** Full regression testing recommended  
**Rollback:** Plan rollback strategy

---

## Version Lifecycle

### Support Policy

| Version | Status | Bug Fixes | Security Fixes | New Features |
|---------|--------|-----------|----------------|--------------|
| **Latest MAJOR** | Supported | Yes | Yes | Yes |
| **Previous MAJOR** | Maintained | Yes | Yes | No |
| **Older versions** | Unsupported | No | No | No |

### Example

When v1.0.0 is released:
- **v1.x:** Fully supported
- **v0.x:** Maintained for 6 months (bug and security fixes)
- **After 6 months:** v0.x unsupported

---

## Pre-Release Versions

### Alpha Releases (X.Y.Z-alpha.N)
- Early development
- Features may change
- Not for production use

```bash
pip install nbctl==0.2.0-alpha.1
```

---

### Beta Releases (X.Y.Z-beta.N)
- Feature complete
- Testing phase
- Use with caution

```bash
pip install nbctl==0.2.0-beta.1
```

---

### Release Candidates (X.Y.Z-rc.N)
- Final testing
- Near production quality
- Safe for testing environments

```bash
pip install nbctl==0.2.0-rc.1
```

---

## Checking for Updates

### Command Line

```bash
# Check current version
nbctl --version

# Compare with PyPI
pip index versions nbctl

# Show outdated packages
pip list --outdated | grep nbctl
```

### Programmatically

```python
import nbctl
print(nbctl.__version__)
```

---

## Release Notes

### Where to Find

- **GitHub Releases:** [github.com/VenkatachalamSubramanianPeriyaSubbu/nbctl/releases](https://github.com/VenkatachalamSubramanianPeriyaSubbu/nbctl/releases)
- **PyPI:** [pypi.org/project/nbctl/#history](https://pypi.org/project/nbctl/#history)
- **CHANGELOG:** `CHANGELOG.md` in repository

### What's Included

- New features
- Bug fixes
- Breaking changes
- Deprecations
- Documentation updates

---

## Pinning Versions

### For Production

Pin to specific version in `requirements.txt`:

```txt
# Pin exact version
nbctl==0.1.0

# Or allow patch updates
nbctl>=0.1.0,<0.2.0
```

### For Development

Allow minor updates in `requirements.txt`:

```txt
# Allow minor and patch updates
nbctl>=0.1.0,<1.0.0
```

---

## Migration Guides

When major versions are released, migration guides are provided:

- **What's changing:** Clear list of breaking changes
- **Why it's changing:** Rationale for changes
- **How to migrate:** Step-by-step instructions
- **Code examples:** Before and after comparisons
- **Deprecation timeline:** When old features are removed

---

## Version History

### v0.1.0 (Current) - November 2025
**Initial Release**

Features:
- 13 comprehensive commands
- Full documentation
- Stable release

Commands:
- clean, info, export, extract
- ml-split, run, lint, format
- git-setup, diff, combine, resolve, security

---

## Questions?

- **About versions:** Check [GitHub Releases](https://github.com/VenkatachalamSubramanianPeriyaSubbu/nbctl/releases)
- **About compatibility:** [Open an issue](https://github.com/VenkatachalamSubramanianPeriyaSubbu/nbctl/issues)
- **About updates:** See [Installation Guide](installation.md)

---

**Stay updated! Star the repo and watch for new releases.**

