# nbutils ml-split

Split ML notebooks into production-ready Python pipeline modules.

## Description

The `ml-split` command automatically transforms machine learning notebooks into well-structured Python packages. It intelligently detects ML workflow sections (data collection, preprocessing, training, etc.) and generates modular Python files with proper structure and dependencies.

Use this command to:
- Convert ML experiments to production code
- Create deployable ML pipelines
- Maintain proper software engineering structure
- Enable automated ML workflows
- Facilitate testing and deployment

## Usage

```bash
nbutils ml-split NOTEBOOK [OPTIONS]
```

## Arguments

| Argument | Description | Required |
|----------|-------------|----------|
| `NOTEBOOK` | Path to the ML Jupyter notebook file | Yes |

## Options

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `--output` | `-o` | PATH | `ml_pipeline/` | Output directory for pipeline |
| `--create-main` | | Flag | True | Create main.py runner script |

## Detected Sections

The command recognizes 7 common ML workflow patterns based on markdown headers:

| Section | Module Name | Triggers |
|---------|-------------|----------|
| **Data Collection** | `data_collection.py` | "data collection", "load data", "import data" |
| **Data Preprocessing** | `data_preprocessing.py` | "preprocessing", "data cleaning", "clean data" |
| **Feature Engineering** | `feature_engineering.py` | "feature engineering", "features", "feature extraction" |
| **Data Splitting** | `data_splitting.py` | "split", "train test split", "validation split" |
| **Model Training** | `model_training.py` | "train", "training", "fit model" |
| **Model Evaluation** | `model_evaluation.py` | "evaluation", "evaluate", "test", "metrics" |
| **Model Saving** | `model_saving.py` | "save", "export model", "serialize" |

## Generated Structure

```
ml_pipeline/
├── __init__.py                  # Package initialization
├── main.py                      # Pipeline runner
├── requirements.txt             # Auto-generated dependencies
├── data_collection.py           # Data loading module
├── data_preprocessing.py        # Cleaning and preprocessing
├── feature_engineering.py       # Feature creation
├── data_splitting.py            # Train/test split
├── model_training.py            # Model training
├── model_evaluation.py          # Evaluation and metrics
└── model_saving.py              # Model persistence
```

## Module Structure

Each generated module follows this pattern:

```python
def run(context=None):
    """
    Execute the [section name] step.
    
    Args:
        context: Dictionary containing variables from previous steps
        
    Returns:
        Dictionary containing all local variables for next steps
    """
    # If context provided, extract variables
    if context:
        # Variables from previous steps available here
        pass
    
    # Your notebook code here
    # ...
    
    # Return all variables for next step
    return locals()
```

## Pipeline Runner (main.py)

The generated `main.py` orchestrates the entire pipeline:

```python
# Execute pipeline in sequence
context = data_collection.run()
context = data_preprocessing.run(context)
context = feature_engineering.run(context)
context = data_splitting.run(context)
context = model_training.run(context)
context = model_evaluation.run(context)
context = model_saving.run(context)

print("Pipeline completed successfully!")
```

## Context Passing

Variables automatically flow between pipeline steps:

```python
# Step 1: Data collection
def run(context=None):
    df = pd.read_csv('data.csv')
    return locals()  # Returns {'df': DataFrame}

# Step 2: Preprocessing (receives df)
def run(context=None):
    if context:
        df = context['df']  # Access df from previous step
    df_clean = preprocess(df)
    return locals()  # Returns {'df': DataFrame, 'df_clean': DataFrame}

# Step 3: Training (receives df and df_clean)
def run(context=None):
    if context:
        df_clean = context['df_clean']  # Access cleaned data
    model = train(df_clean)
    return locals()
```

## Requirements Generation

Dependencies are automatically extracted from imports:

```python
# Detected imports in notebook
import pandas
import numpy
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot

# Generated requirements.txt
pandas>=1.0.0
numpy>=1.19.0
scikit-learn>=0.24.0
matplotlib>=3.0.0
```

## Output Messages

### Success

```
ML Pipeline created successfully!

Generated modules:
  - data_collection.py (15 lines)
  - data_preprocessing.py (42 lines)
  - feature_engineering.py (28 lines)
  - model_training.py (35 lines)
  - model_evaluation.py (22 lines)
  - main.py (runner)
  - requirements.txt (5 dependencies)

Output directory: ml_pipeline/

To run the pipeline:
  cd ml_pipeline
  pip install -r requirements.txt
  python main.py
```

### Warnings

```
⚠ Warning: No section headers detected
  Consider adding markdown headers to organize your notebook:
  # Data Collection
  # Data Preprocessing
  # Model Training
  etc.

  All code will be placed in a single module.
```

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success, pipeline generated |
| 1 | File not found or invalid notebook |
| 2 | No code cells found |
| 3 | Output directory creation failed |

## Notes

- **Section detection:** Based on markdown headers (case-insensitive)
- **Code grouping:** Code cells are grouped by their nearest preceding header
- **Import extraction:** All import statements are collected for requirements.txt
- **Context preservation:** Variables flow between steps automatically
- **Runnable immediately:** Generated pipeline can be executed right away
- **No notebook dependency:** Generated code doesn't require Jupyter

## Best Practices

### Notebook Organization

Structure your notebook with clear markdown headers:

```markdown
# Data Collection
[code cells for loading data]

# Data Preprocessing
[code cells for cleaning]

# Feature Engineering
[code cells for feature creation]

# Model Training
[code cells for training]

# Model Evaluation
[code cells for evaluation]
```

### Variable Naming

Use consistent variable names that make sense across steps:

- `df` for main DataFrame
- `X_train`, `X_test` for features
- `y_train`, `y_test` for labels
- `model` for trained model

### Module Independence

While modules can access context:
- Minimize dependencies between steps
- Make each step as self-contained as possible
- Document expected inputs and outputs

## Related Commands

- [`run`](run.md) - Execute the generated pipeline
- [`info`](info.md) - Analyze notebook before splitting
- [`extract`](extract.md) - Extract outputs for analysis

## See Also

- [Examples](../examples/ml-split.md) - Practical usage examples
- [Getting Started](../getting-started/welcome.md) - Introduction to nbutils

