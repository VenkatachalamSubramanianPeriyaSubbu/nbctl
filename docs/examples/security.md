# Security Command Examples

Practical examples for scanning notebooks for security vulnerabilities.

## Basic Usage

### Scan Notebook

```bash
nbctl security notebook.ipynb
```

### High Severity Only

```bash
nbctl security notebook.ipynb --severity high
```

### With Recommendations

```bash
nbctl security notebook.ipynb --verbose
```

### JSON Output

```bash
nbctl security notebook.ipynb --json
```

## Severity Filtering

### All Issues (Default)

```bash
nbctl security notebook.ipynb --severity all
```

### Medium and Above

```bash
nbctl security notebook.ipynb --severity medium
```

### Low Severity Only

```bash
nbctl security notebook.ipynb --severity low
```

## Workflow Examples

### Pre-Commit Security Check

```bash
#!/bin/bash
# .git/hooks/pre-commit

for nb in $(git diff --cached --name-only | grep '\.ipynb$'); do
    echo "Scanning $nb..."
    if ! nbctl security "$nb" --severity high; then
        echo "Security issues found in $nb"
        echo "Fix issues before committing"
        exit 1
    fi
done

echo "Security scan passed"
```

### CI/CD Security Scan

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

### Batch Scanning

```bash
#!/bin/bash
# Scan all notebooks in project

echo "Security Scan Report" > security-report.txt
echo "====================" >> security-report.txt

for nb in **/*.ipynb; do
    echo -e "\n$nb:" >> security-report.txt
    nbctl security "$nb" --severity high >> security-report.txt 2>&1
done

echo "Security report: security-report.txt"
```

## Advanced Examples

### Scan with Categorized Output

```bash
#!/bin/bash
# Generate categorized security report

date=$(date +%Y-%m-%d)
report="security-scan-$date.txt"

echo "Security Scan - $date" > "$report"
echo "=====================" >> "$report"

for severity in high medium low; do
    echo -e "\n=== $severity SEVERITY ===" >> "$report"
    for nb in *.ipynb; do
        result=$(nbctl security "$nb" --severity $severity 2>&1)
        if [ -n "$result" ]; then
            echo -e "\n$nb:" >> "$report"
            echo "$result" >> "$report"
        fi
    done
done

echo "Report: $report"
```

### Generate JSON Security Database

```bash
#!/bin/bash
# Create JSON database of all security issues

echo "[" > security-db.json
first=true

for nb in *.ipynb; do
    if ! $first; then
        echo "," >> security-db.json
    fi
    first=false
    
    nbctl security "$nb" --json >> security-db.json
done

echo "]" >> security-db.json
echo "Security database: security-db.json"
```

### Track Security Over Time

```bash
#!/bin/bash
# Track security issues in CSV

date=$(date +%Y-%m-%d)
nb="$1"

high=$(nbctl security "$nb" --severity high 2>&1 | grep -c "HIGH" || echo "0")
medium=$(nbctl security "$nb" --severity medium 2>&1 | grep -c "MEDIUM" || echo "0")
low=$(nbctl security "$nb" --severity low 2>&1 | grep -c "LOW" || echo "0")

echo "$date,$high,$medium,$low" >> security-history.csv
```

### Automated Remediation Helper

```bash
#!/bin/bash
# Scan and create remediation task list

nb="$1"
output="remediation-$(basename $nb .ipynb).md"

echo "# Security Remediation: $nb" > "$output"
echo "Generated: $(date)" >> "$output"
echo >> "$output"

nbctl security "$nb" --verbose >> "$output"

echo -e "\n## Checklist" >> "$output"
echo "- [ ] Review all HIGH severity issues" >> "$output"
echo "- [ ] Fix or document exceptions" >> "$output"
echo "- [ ] Re-scan after fixes" >> "$output"
echo "- [ ] Update security documentation" >> "$output"

echo "Remediation plan: $output"
```

## Integration Examples

### Pre-Commit Hook with Auto-Fix Hints

```bash
#!/bin/bash
# .git/hooks/pre-commit

RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

failed=false

for nb in $(git diff --cached --name-only | grep '\.ipynb$'); do
    echo -e "${YELLOW}Scanning $nb...${NC}"
    
    if ! nbctl security "$nb" --severity high --quiet; then
        echo -e "${RED}Security issues found in $nb${NC}"
        echo -e "${YELLOW}Run: nbctl security $nb --verbose${NC}"
        failed=true
    else
        echo -e "${GREEN}$nb passed security scan${NC}"
    fi
done

if $failed; then
    echo -e "\n${RED}Commit blocked due to security issues${NC}"
    exit 1
fi
```

### GitLab CI with Artifacts

```yaml
security-scan:
  stage: test
  script:
    - pip install nbctl
    - |
      mkdir -p security-reports
      for nb in *.ipynb; do
        nbctl security "$nb" --json > "security-reports/${nb%.ipynb}.json"
      done
  artifacts:
    reports:
      paths:
        - security-reports/
    expire_in: 30 days
  only:
    - merge_requests
```

### Weekly Security Audit

```bash
#!/bin/bash
# weekly-security-audit.sh

week=$(date +%Y-W%U)
report_dir="security-audits/week-$week"

mkdir -p "$report_dir"

# Scan all notebooks
for nb in **/*.ipynb; do
    name=$(echo "$nb" | tr '/' '_')
    nbctl security "$nb" --verbose > "$report_dir/${name%.ipynb}.txt"
done

# Generate summary
total_high=0
total_medium=0
total_low=0

for report in "$report_dir"/*.txt; do
    high=$(grep -c "\[HIGH\]" "$report" || echo "0")
    medium=$(grep -c "\[MEDIUM\]" "$report" || echo "0")
    low=$(grep -c "\[LOW\]" "$report" || echo "0")
    
    total_high=$((total_high + high))
    total_medium=$((total_medium + medium))
    total_low=$((total_low + low))
done

echo "Weekly Security Audit - Week $week" > "$report_dir/SUMMARY.txt"
echo "===================================" >> "$report_dir/SUMMARY.txt"
echo "High: $total_high" >> "$report_dir/SUMMARY.txt"
echo "Medium: $total_medium" >> "$report_dir/SUMMARY.txt"
echo "Low: $total_low" >> "$report_dir/SUMMARY.txt"

echo "Weekly audit complete: $report_dir"
```

## Real-World Examples

### Find All Hardcoded Secrets

```bash
#!/bin/bash
# Find notebooks with hardcoded secrets

echo "Notebooks with hardcoded secrets:"
echo "================================="

for nb in **/*.ipynb; do
    if nbctl security "$nb" --severity high 2>&1 | grep -q "Hardcoded"; then
        echo "⚠ $nb"
        nbctl security "$nb" --severity high 2>&1 | grep "Hardcoded"
    fi
done
```

### SQL Injection Audit

```bash
#!/bin/bash
# Find notebooks with SQL injection risks

for nb in **/*.ipynb; do
    if nbctl security "$nb" --severity high 2>&1 | grep -q "SQL"; then
        echo "=== $nb ==="
        nbctl security "$nb" --verbose 2>&1 | grep -A 10 "SQL"
        echo
    fi
done
```

### Security Dashboard

```bash
#!/bin/bash
# Generate HTML security dashboard

cat > security-dashboard.html << 'EOF'
<html>
<head><title>Security Dashboard</title></head>
<body>
<h1>Notebook Security Dashboard</h1>
<table border="1">
<tr><th>Notebook</th><th>High</th><th>Medium</th><th>Low</th></tr>
EOF

for nb in *.ipynb; do
    high=$(nbctl security "$nb" --severity high 2>&1 | grep -c "\[HIGH\]" || echo "0")
    medium=$(nbctl security "$nb" --severity medium 2>&1 | grep -c "\[MEDIUM\]" || echo "0")
    low=$(nbctl security "$nb" --severity low 2>&1 | grep -c "\[LOW\]" || echo "0")
    
    echo "<tr><td>$nb</td><td>$high</td><td>$medium</td><td>$low</td></tr>" >> security-dashboard.html
done

echo "</table></body></html>" >> security-dashboard.html
echo "Dashboard: security-dashboard.html"
```

## Tips & Best Practices

### 1. Scan Regularly

```bash
# Daily security check
for nb in *.ipynb; do
    nbctl security "$nb" --severity high
done
```

### 2. Focus on High Severity First

```bash
# Fix critical issues first
nbctl security notebook.ipynb --severity high --verbose
```

### 3. Use in CI/CD

```bash
# Block merges with security issues
nbctl security *.ipynb --severity high || exit 1
```

### 4. Document Exceptions

If an issue is a false positive:

```python
# SECURITY: This is not a real API key, it's a test value
api_key = "test-key-12345"
```

### 5. Rotate Exposed Secrets

If secrets are found:

```bash
# 1. Scan and identify
nbctl security notebook.ipynb --verbose

# 2. Remove from notebook
# 3. Rotate/revoke the exposed secrets
# 4. Use environment variables
# 5. Re-scan to verify
```

## Related Examples

- [Clean Examples](clean.md) - Remove outputs (may contain secrets)
- [Lint Examples](lint.md) - Check code quality
- [Git-Setup Examples](git-setup.md) - Configure pre-commit hooks

