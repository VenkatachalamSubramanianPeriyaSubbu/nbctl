# nbctl security

Scan notebooks for security vulnerabilities and secrets.

## Description

The `security` command scans Jupyter notebooks for security issues, including hardcoded secrets, unsafe code patterns, and potential vulnerabilities. It helps prevent accidental exposure of sensitive information and identifies risky code before it reaches production.

Use this command to:
- Find hardcoded API keys, passwords, and tokens
- Detect SQL injection risks
- Identify unsafe deserialization
- Find command injection vulnerabilities
- Detect weak cryptography
- Prevent security breaches
- Enable security checks in CI/CD

## Usage

```bash
nbctl security NOTEBOOK [OPTIONS]
```

## Arguments

| Argument | Description | Required |
|----------|-------------|----------|
| `NOTEBOOK` | Path to the Jupyter notebook file | Yes |

## Options

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `--severity` | | TEXT | `all` | Filter by severity: `low`, `medium`, `high`, `all` |
| `--json` | | Flag | False | Output as JSON for automation |
| `--verbose` | `-v` | Flag | False | Show detailed recommendations |

## Security Checks

### HIGH Severity

Critical issues that should be fixed immediately:

#### 1. Hardcoded Secrets
Detects API keys, passwords, tokens, and other credentials.

**Patterns detected:**
- `api_key = "sk-..."`
- `password = "secret123"`
- `token = "ghp_..."`
- `AWS_SECRET_ACCESS_KEY = "..."`
- Database connection strings with credentials
- Private keys

**Risk:** Credentials exposed in version control, public repos

---

#### 2. Unsafe Pickle Deserialization
Detects use of `pickle.load()` or `pickle.loads()`.

**Pattern detected:**
```python
import pickle
model = pickle.load(file)
```

**Risk:** Arbitrary code execution from untrusted pickle files

---

#### 3. SQL Injection
Detects string concatenation in SQL queries.

**Pattern detected:**
```python
query = f"SELECT * FROM users WHERE id = {user_id}"
cursor.execute(query)
```

**Risk:** SQL injection attacks, data breach

---

### MEDIUM Severity

Important issues that should be addressed:

#### 4. Command Injection
Detects dangerous functions: `os.system()`, `eval()`, `exec()`.

**Pattern detected:**
```python
os.system(f"rm {filename}")
eval(user_input)
exec(code_string)
```

**Risk:** Arbitrary command/code execution

---

#### 5. Unsafe YAML Parsing
Detects `yaml.load()` without SafeLoader.

**Pattern detected:**
```python
import yaml
data = yaml.load(file)  # Unsafe!
```

**Risk:** Arbitrary code execution via YAML

---

#### 6. Disabled SSL Verification
Detects disabled certificate verification.

**Pattern detected:**
```python
requests.get(url, verify=False)
urllib3.disable_warnings()
```

**Risk:** Man-in-the-middle attacks

---

### LOW Severity

Minor issues to consider:

#### 7. Weak Cryptographic Algorithms
Detects use of MD5, SHA1, or weak ciphers.

**Pattern detected:**
```python
import hashlib
hash = hashlib.md5(data)
hash = hashlib.sha1(data)
```

**Risk:** Cryptographic weakness, hash collisions

---

## Output

### Default Output (All Issues)

```bash
nbctl security notebook.ipynb
```

Output:
```
Security Scan: notebook.ipynb

HIGH SEVERITY ISSUES (3):

  [HIGH] Hardcoded Secret - Cell 5
  ├─ Type: API Key
  ├─ Pattern: api_key = "sk-proj-..."
  └─ Line: 3

  [HIGH] SQL Injection Risk - Cell 12
  ├─ Type: String concatenation in SQL
  ├─ Pattern: f"SELECT * FROM users WHERE id = {user_id}"
  └─ Line: 7

  [HIGH] Unsafe Pickle - Cell 18
  ├─ Type: Unsafe deserialization
  ├─ Pattern: pickle.load(file)
  └─ Line: 2

MEDIUM SEVERITY ISSUES (2):

  [MEDIUM] Command Injection - Cell 8
  ├─ Type: os.system() usage
  ├─ Pattern: os.system(f"rm {filename}")
  └─ Line: 5

  [MEDIUM] Disabled SSL - Cell 15
  ├─ Type: SSL verification disabled
  ├─ Pattern: requests.get(url, verify=False)
  └─ Line: 3

LOW SEVERITY ISSUES (1):

  [LOW] Weak Cryptography - Cell 20
  ├─ Type: MD5 usage
  ├─ Pattern: hashlib.md5(data)
  └─ Line: 4

Summary:
  Total issues: 6
  High: 3 | Medium: 2 | Low: 1

⚠ Action required: Fix HIGH severity issues immediately
```

---

### Filtered by Severity

```bash
nbctl security notebook.ipynb --severity high
```

Output:
```
Security Scan: notebook.ipynb
Filtering: HIGH severity only

HIGH SEVERITY ISSUES (3):

  [HIGH] Hardcoded Secret - Cell 5
  [HIGH] SQL Injection Risk - Cell 12
  [HIGH] Unsafe Pickle - Cell 18

Summary: 3 HIGH severity issues found
```

---

### Verbose Output

```bash
nbctl security notebook.ipynb --verbose
```

Includes detailed recommendations:

```
[HIGH] Hardcoded Secret - Cell 5

Issue:
  api_key = "sk-proj-abc123..."

Risk:
  API keys in code can be exposed via:
  - Version control history
  - Public repositories
  - Log files
  - Screenshots

Recommendation:
  Use environment variables:
    import os
    api_key = os.getenv('API_KEY')

  Use config files (not committed):
    import configparser
    config = configparser.ConfigParser()
    config.read('config.ini')
    api_key = config['API']['key']

  Use secret management:
    - AWS Secrets Manager
    - HashiCorp Vault
    - Azure Key Vault

  Rotate the exposed key immediately

References:
  - OWASP A02:2021 – Cryptographic Failures
  - CWE-798: Use of Hard-coded Credentials
```

---

### JSON Output

```bash
nbctl security notebook.ipynb --json
```

Output:
```json
{
  "notebook": "notebook.ipynb",
  "scan_date": "2025-11-12T10:30:00Z",
  "issues": [
    {
      "severity": "HIGH",
      "type": "hardcoded_secret",
      "cell": 5,
      "line": 3,
      "pattern": "api_key = \"sk-proj-...\"",
      "description": "Hardcoded API key detected",
      "cwe": "CWE-798",
      "owasp": "A02:2021"
    },
    {
      "severity": "HIGH",
      "type": "sql_injection",
      "cell": 12,
      "line": 7,
      "pattern": "f\"SELECT * FROM users WHERE id = {user_id}\"",
      "description": "SQL injection risk via string concatenation",
      "cwe": "CWE-89",
      "owasp": "A03:2021"
    }
  ],
  "summary": {
    "total": 6,
    "high": 3,
    "medium": 2,
    "low": 1
  }
}
```

## Secret Detection Patterns

### API Keys

| Service | Pattern Example |
|---------|----------------|
| **OpenAI** | `sk-proj-...`, `sk-...` |
| **AWS** | `AKIA...`, `AWS_SECRET_ACCESS_KEY` |
| **GitHub** | `ghp_...`, `gho_...` |
| **Stripe** | `sk_live_...`, `pk_live_...` |
| **Slack** | `xoxb-...`, `xoxp-...` |
| **Google** | `AIza...` |
| **JWT** | `eyJ...` (base64 JWT pattern) |

### Database Credentials

```python
# Detected patterns
db_password = "secret123"
DATABASE_URL = "postgresql://user:pass@host/db"
connection_string = "Server=...;Password=..."
```

### Private Keys

```python
# Detected patterns
private_key = "-----BEGIN PRIVATE KEY-----"
ssh_key = "-----BEGIN RSA PRIVATE KEY-----"
```

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | No issues found (clean) |
| 1 | Issues found |
| 2 | File not found or invalid notebook |

## Severity Filtering

| Filter | Shows |
|--------|-------|
| `--severity all` | All issues (default) |
| `--severity high` | Only HIGH severity |
| `--severity medium` | Only MEDIUM severity |
| `--severity low` | Only LOW severity |

## Fixing Security Issues

### 1. Hardcoded Secrets

**Bad:**
```python
api_key = "sk-proj-abc123..."
```

**Good:**
```python
import os
api_key = os.getenv('OPENAI_API_KEY')
```

---

### 2. SQL Injection

**Bad:**
```python
query = f"SELECT * FROM users WHERE id = {user_id}"
cursor.execute(query)
```

**Good:**
```python
query = "SELECT * FROM users WHERE id = ?"
cursor.execute(query, (user_id,))
```

---

### 3. Unsafe Pickle

**Bad:**
```python
import pickle
model = pickle.load(file)
```

**Good:**
```python
import joblib  # Safer alternative
model = joblib.load(file)

# Or use safetensors, onnx, etc.
```

---

### 4. Command Injection

**Bad:**
```python
os.system(f"rm {filename}")
```

**Good:**
```python
import subprocess
subprocess.run(['rm', filename], check=True)

# Or better, use pathlib
from pathlib import Path
Path(filename).unlink()
```

---

### 5. Unsafe YAML

**Bad:**
```python
data = yaml.load(file)
```

**Good:**
```python
data = yaml.safe_load(file)
```

---

### 6. Disabled SSL

**Bad:**
```python
requests.get(url, verify=False)
```

**Good:**
```python
requests.get(url)  # verify=True by default
```

---

### 7. Weak Cryptography

**Bad:**
```python
hash = hashlib.md5(data)
```

**Good:**
```python
hash = hashlib.sha256(data)
# Or sha3_256, blake2b, etc.
```

## CI/CD Integration

### Fail Build on Issues

```bash
# Fail if any issues found
nbctl security notebook.ipynb || exit 1

# Fail only on HIGH severity
nbctl security notebook.ipynb --severity high || exit 1

# Generate report for CI
nbctl security notebook.ipynb --json > security-report.json
```

---

### GitHub Actions Example

```yaml
name: Security Scan
on: [push, pull_request]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install nbctl
        run: pip install nbctl
      - name: Scan notebooks
        run: |
          for nb in *.ipynb; do
            nbctl security "$nb" --severity high || exit 1
          done
```

## Notes

- **Read-only:** Never modifies the notebook
- **Static analysis:** Doesn't execute code
- **Pattern-based:** Uses regex and heuristics
- **False positives:** May flag legitimate code (review carefully)
- **False negatives:** May miss sophisticated attacks
- **Complementary:** Use with other security tools

## Best Practices

### 1. Scan Before Commit

```bash
# Pre-commit workflow
nbctl security notebook.ipynb --severity high
git add notebook.ipynb
git commit
```

### 2. Regular Scans

```bash
# Scan all notebooks regularly
for nb in *.ipynb; do
    nbctl security "$nb"
done
```

### 3. CI/CD Integration

```bash
# In CI pipeline
nbctl security *.ipynb --json > security-report.json
```

### 4. Fix High Severity First

```bash
# Focus on critical issues
nbctl security notebook.ipynb --severity high --verbose
```

## Limitations

- **Pattern-based:** May not catch all vulnerabilities
- **No execution:** Can't detect runtime vulnerabilities
- **False positives:** May flag safe code
- **Obfuscation:** Can't detect heavily obfuscated secrets
- **Context-unaware:** Doesn't understand business logic

**Use alongside:**
- Manual security review
- Penetration testing
- Dependency scanning (pip-audit, safety)
- Secret scanning (git-secrets, truffleHog)

## Related Commands

- [`clean`](clean.md) - Remove outputs (may contain secrets)
- [`lint`](lint.md) - Check code quality
- [`info`](info.md) - Analyze dependencies
- [`format`](format.md) - Format code

## See Also

- [Examples](../examples/security.md) - Practical usage examples
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - Web security risks
- [CWE](https://cwe.mitre.org/) - Common Weakness Enumeration
- [Getting Started](../getting-started/welcome.md) - Introduction to nbctl

