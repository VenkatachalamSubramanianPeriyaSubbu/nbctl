# Run Command Examples

Practical examples for executing notebooks from the command line.

## Basic Execution

### Run Single Notebook

```bash
nbctl run analysis.ipynb
```

### Run Multiple Notebooks

```bash
nbctl run 01_load.ipynb 02_process.ipynb 03_analyze.ipynb
```

### Run All Notebooks

```bash
nbctl run *.ipynb
```

### Run in Alphabetical Order

```bash
nbctl run *.ipynb --order
```

## With Options

### Set Timeout

```bash
nbctl run notebook.ipynb --timeout 600  # 10 minutes per cell
```

### Continue on Errors

```bash
nbctl run notebook.ipynb --allow-errors
```

### Save Executed Notebooks

```bash
nbctl run notebook.ipynb --save-output ./executed/
```

### Use Different Kernel

```bash
nbctl run notebook.ipynb --kernel python3
```

## Workflow Examples

### ML Training Pipeline

```bash
#!/bin/bash
# Run ML notebooks in sequence

nbctl run \
    01_data_prep.ipynb \
    02_feature_engineering.ipynb \
    03_model_training.ipynb \
    04_evaluation.ipynb \
    --timeout 3600 \
    --save-output ./trained_models/

echo "ML pipeline completed"
```

### Nightly Report Generation

```bash
#!/bin/bash
# Generate reports overnight

# Run analysis notebooks
nbctl run reports/*.ipynb --save-output ./generated/

# Export to HTML
for nb in generated/*.ipynb; do
    nbctl export "$nb" -f html --output-dir ./reports/html/
done

echo "Reports generated"
```

### Data Processing Pipeline

```bash
# Process data files in sequence
nbctl run \
    data_cleaning.ipynb \
    data_validation.ipynb \
    data_export.ipynb \
    --allow-errors \
    --save-output ./processed/
```

## CI/CD Examples

### GitHub Actions

```yaml
name: Run Notebooks
on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2
      - name: Install dependencies
        run: |
          pip install nbctl
          pip install -r requirements.txt
      - name: Run test notebooks
        run: |
          nbctl run tests/*.ipynb --timeout 300
```

### GitLab CI

```yaml
test-notebooks:
  script:
    - pip install nbctl
    - nbctl run tests/*.ipynb --allow-errors
  artifacts:
    paths:
      - test-results/
```

## Advanced Examples

### Batch Processing with Logging

```bash
#!/bin/bash
# Run notebooks with logging

log_file="execution-$(date +%Y%m%d).log"

for nb in *.ipynb; do
    echo "Running $nb..." | tee -a "$log_file"
    if nbctl run "$nb" --timeout 600; then
        echo "Success: $nb" | tee -a "$log_file"
    else
        echo "Failed: $nb" | tee -a "$log_file"
    fi
done
```

### Conditional Execution

```bash
# Run only if file changed
if git diff --name-only HEAD~1 | grep -q "analysis.ipynb"; then
    echo "Running updated notebook..."
    nbctl run analysis.ipynb --save-output ./results/
fi
```

### Parallel Execution

```bash
# Run notebooks in parallel (using GNU parallel)
parallel nbctl run {} ::: *.ipynb
```

### Retry on Failure

```bash
#!/bin/bash
max_retries=3
nb="flaky_notebook.ipynb"

for i in $(seq 1 $max_retries); do
    if nbctl run "$nb"; then
        echo "Success on attempt $i"
        break
    else
        echo "Failed attempt $i"
        sleep 60
    fi
done
```

## Tips & Best Practices

### 1. Test Locally First

```bash
# Test with short timeout
nbctl run notebook.ipynb --timeout 60

# If OK, run with longer timeout
nbctl run notebook.ipynb --timeout 3600
```

### 2. Save Outputs for Review

```bash
# Always save outputs for debugging
nbctl run notebook.ipynb --save-output ./executed/
```

### 3. Use Timeouts in CI/CD

```bash
# Prevent hanging builds
nbctl run notebook.ipynb --timeout 300
```

### 4. Handle Long-Running Notebooks

```bash
# No timeout for ML training
nbctl run train_model.ipynb
```

## Related Examples

- [Clean Examples](clean.md) - Clean after execution
- [Export Examples](export.md) - Export executed notebooks
- [ML-Split Examples](ml-split.md) - Convert to Python pipeline

