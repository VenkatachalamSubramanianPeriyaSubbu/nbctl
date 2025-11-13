# ML-Split Command Examples

Practical examples for using `nbctl ml-split` to create production ML pipelines.

## Basic Usage

### Split ML Notebook

```bash
nbctl ml-split ml_model.ipynb
```

**Result:**
```
ml_pipeline/
├── __init__.py
├── main.py
├── requirements.txt
├── data_collection.py
├── data_preprocessing.py
├── feature_engineering.py
├── model_training.py
└── model_evaluation.py
```

### Custom Output Directory

```bash
nbctl ml-split ml_model.ipynb --output src/ml/
```

### Run Generated Pipeline

```bash
cd ml_pipeline
pip install -r requirements.txt
python main.py
```

## Notebook Structure

### Organize Your Notebook

Structure with clear headers for best results:

```markdown
# Data Collection
[code to load data]

# Data Preprocessing
[code to clean data]

# Feature Engineering
[code to create features]

# Model Training
[code to train model]

# Model Evaluation
[code to evaluate model]
```

## Generated Code Examples

### Module Structure

Each generated module:

```python
# data_collection.py
def run(context=None):
    """Execute data collection step."""
    import pandas as pd
    
    # Load data
    df = pd.read_csv('data.csv')
    
    # Return variables for next step
    return locals()
```

### Main Pipeline

Generated `main.py`:

```python
import data_collection
import data_preprocessing
import model_training

# Execute pipeline
context = data_collection.run()
context = data_preprocessing.run(context)
context = model_training.run(context)

print("Pipeline completed successfully!")
```

## Complete Workflow

### From Notebook to Production

```bash
#!/bin/bash
# notebook-to-production.sh

# 1. Develop in notebook
# (work on ml_experiment.ipynb)

# 2. Split into pipeline
nbctl ml-split ml_experiment.ipynb --output ml_pipeline/

# 3. Set up Python package
cd ml_pipeline/
pip install -r requirements.txt

# 4. Test pipeline
python main.py

# 5. Deploy
# Copy ml_pipeline/ to production server
```

## Advanced Examples

### Multiple ML Notebooks

Split multiple experiments:

```bash
#!/bin/bash
# split-all-experiments.sh

for nb in experiments/*.ipynb; do
    name=$(basename "$nb" .ipynb)
    nbctl ml-split "$nb" --output "pipelines/$name/"
done

echo "All notebooks split into pipelines"
```

### Custom Pipeline Structure

```bash
# Split to specific directory structure
nbctl ml-split ml_model.ipynb --output src/models/classifier/

# Result:
# src/models/classifier/
# ├── data_collection.py
# ├── model_training.py
# └── ...
```

### Testing Generated Pipeline

```bash
# Split notebook
nbctl ml-split ml_model.ipynb

# Test pipeline
cd ml_pipeline

# Install dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/  # if you add tests

# Run pipeline
python main.py
```

## Real-World Examples

### Image Classification Pipeline

Notebook structure:

```markdown
# Data Collection
- Load image dataset
- Download from S3

# Data Preprocessing
- Resize images
- Normalize pixels

# Data Augmentation
- Random flips
- Color jittering

# Model Training
- Define CNN architecture
- Train with callbacks

# Model Evaluation
- Calculate accuracy
- Generate confusion matrix

# Model Saving
- Save model weights
- Export to ONNX
```

Split and run:

```bash
nbctl ml-split image_classifier.ipynb --output image_pipeline/
cd image_pipeline/
python main.py
```

### NLP Pipeline

Notebook structure:

```markdown
# Data Collection
- Load text corpus
- Download pretrained model

# Data Preprocessing
- Tokenization
- Cleaning text

# Feature Engineering
- TF-IDF vectors
- Word embeddings

# Model Training
- Fine-tune BERT
- Train classifier

# Model Evaluation
- Calculate F1 score
- Classification report
```

### Time Series Forecasting

```markdown
# Data Collection
- Load historical data
- Fetch from API

# Data Preprocessing
- Handle missing values
- Normalize features

# Feature Engineering
- Create lag features
- Rolling statistics

# Data Splitting
- Train/val/test split
- Time-based split

# Model Training
- Train LSTM
- Hyperparameter tuning

# Model Evaluation
- RMSE, MAE metrics
- Plot predictions
```

## CI/CD Integration

### GitHub Actions

`.github/workflows/ml-pipeline.yml`:

```yaml
name: ML Pipeline
on: [push]

jobs:
  test-pipeline:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Setup Python
        uses: actions/setup-python@v2
        
      - name: Install nbctl
        run: pip install nbctl
      
      - name: Generate pipeline
        run: |
          nbctl ml-split notebooks/ml_model.ipynb --output ml_pipeline/
      
      - name: Test pipeline
        run: |
          cd ml_pipeline
          pip install -r requirements.txt
          python main.py
```

### Docker Deployment

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy generated pipeline
COPY ml_pipeline/ /app/

# Install dependencies
RUN pip install -r requirements.txt

# Run pipeline
CMD ["python", "main.py"]
```

Build and run:

```bash
docker build -t ml-pipeline .
docker run ml-pipeline
```

## Customization Examples

### Add Logging

Modify generated `main.py`:

```python
import logging
import data_collection
import model_training

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Execute pipeline with logging
logger.info("Starting pipeline...")
context = data_collection.run()
logger.info("Data collected")

context = model_training.run(context)
logger.info("Model trained")

logger.info("Pipeline completed!")
```

### Add Error Handling

```python
import sys
import data_collection
import model_training

try:
    context = data_collection.run()
    context = model_training.run(context)
    print("Pipeline completed successfully")
except Exception as e:
    print(f"Pipeline failed: {e}")
    sys.exit(1)
```

### Add Configuration

Create `config.py`:

```python
# config.py
DATA_PATH = 'data/train.csv'
MODEL_PATH = 'models/classifier.pkl'
BATCH_SIZE = 32
EPOCHS = 10
```

Use in pipeline:

```python
import config
import data_collection

context = data_collection.run()
context['data_path'] = config.DATA_PATH
```

## Tips & Best Practices

### 1. Organize Notebook Well

```markdown
Use clear section headers:
# Data Collection (not "Load stuff")
# Model Training (not "Training the model")
```

### 2. Test Before Splitting

```bash
# Run notebook to verify it works
nbctl run ml_model.ipynb

# Then split
nbctl ml-split ml_model.ipynb
```

### 3. Version Your Pipeline

```bash
# Version 1
nbctl ml-split ml_model.ipynb --output ml_pipeline_v1/

# Version 2 (after improvements)
nbctl ml-split ml_model.ipynb --output ml_pipeline_v2/
```

### 4. Document Generated Code

Add docstrings to generated modules:

```python
# In data_collection.py
def run(context=None):
    """
    Data Collection Step
    
    Loads training data from CSV files.
    
    Returns:
        dict: Contains 'df' (DataFrame) and 'labels'
    """
    # ... generated code ...
```

## Troubleshooting

### No Sections Detected

If no markdown headers:

```bash
# Add headers to notebook
# Data Collection
# Data Preprocessing
# etc.

# Then split again
nbctl ml-split ml_model.ipynb
```

### Module Import Errors

```bash
# Ensure all dependencies installed
cd ml_pipeline/
pip install -r requirements.txt

# Or add missing dependencies
pip install scikit-learn pandas numpy
```

### Context Passing Issues

Ensure variable names are consistent:

```python
# In data_collection.py
df = pd.read_csv(...)
return locals()  # Returns {'df': ...}

# In preprocessing.py
if context:
    df = context['df']  # Use same name
```

## Related Examples

- [Run Examples](run.md) - Execute notebooks before splitting
- [Info Examples](info.md) - Analyze before splitting
- [Extract Examples](extract.md) - Extract results

## Next Steps

- [Deploy ML pipelines](https://docs.python.org/3/tutorial/modules.html)
- [Add unit tests](https://docs.pytest.org/)
- [Containerize with Docker](https://docker.com)

