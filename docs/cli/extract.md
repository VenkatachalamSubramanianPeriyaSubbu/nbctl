# nbctl extract

Extract outputs (images, graphs, data) from notebook cells.

## Description

The `extract` command extracts all outputs from your Jupyter notebook and saves them as separate files. This includes plots, images, data tables, CSV files, JSON data, and text outputs.

Use this command to:
- Save visualizations for reports or publications
- Extract data tables and analysis results
- Archive notebook outputs separately
- Share results without sharing the notebook
- Include figures in documentation

## Usage

```bash
nbctl extract NOTEBOOK [OPTIONS]
```

## Arguments

| Argument | Description | Required |
|----------|-------------|----------|
| `NOTEBOOK` | Path to the Jupyter notebook file | Yes |

## Options

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `--output` | `-o` | PATH | `outputs/` | Output directory for extracted files |
| `--data` | | Flag | False | Extract only data outputs |
| `--images` | | Flag | False | Extract only image outputs |
| `--all` | | Flag | False | Extract all without prompting |

## Output Structure

Extracted files are organized into subdirectories:

```
outputs/
├── data/
│   ├── cell_0_output_0_data_0.json
│   ├── cell_1_output_0_data_1.html      # DataFrame
│   ├── cell_2_output_0_data_2.csv
│   └── cell_3_output_0_data_3.txt
└── images/
    ├── cell_4_output_0_img_0.png        # Matplotlib plot
    ├── cell_5_output_0_img_1.svg        # Vector graphic
    └── cell_6_output_0_img_2.jpeg
```

### File Naming Convention

Format: `cell_{cell_idx}_output_{output_idx}_{type}_{counter}.{ext}`

- **cell_idx:** Cell number in notebook (0-indexed)
- **output_idx:** Output number within cell (0-indexed)
- **type:** `data` or `img`
- **counter:** Sequential counter for type
- **ext:** File extension based on content type

## Extracted Types

### Image Outputs

| Format | Extension | Description |
|--------|-----------|-------------|
| PNG | `.png` | Raster images, plots |
| JPEG | `.jpeg` | Compressed images |
| SVG | `.svg` | Vector graphics, scalable plots |

**Common sources:**
- Matplotlib/Seaborn plots
- PIL/Pillow images
- Plotly visualizations
- Image display outputs

### Data Outputs

| Format | Extension | Description |
|--------|-----------|-------------|
| JSON | `.json` | JSON data structures |
| HTML | `.html` | HTML tables (pandas DataFrames) |
| CSV | `.csv` | Comma-separated values |
| Text | `.txt` | Plain text outputs |

**Common sources:**
- Pandas DataFrame displays
- JSON API responses
- Data summaries
- Model evaluation metrics

## Interactive Mode

When run without `--data`, `--images`, or `--all`, the command prompts:

```
What would you like to extract?
1. Both data and images
2. Only data outputs
3. Only image outputs
4. All outputs without prompting

Enter choice (1-4):
```

## Output Summary

```
Extraction Summary:

Images extracted:
cell_4_output_0_img_0.png
cell_5_output_0_img_1.svg
cell_6_output_0_img_2.jpeg

Data extracted:
cell_0_output_0_data_0.json
cell_1_output_0_data_1.html
cell_2_output_0_data_2.csv

Total: 3 images, 3 data files
Saved to: outputs/
```

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success, outputs extracted |
| 1 | File not found or invalid notebook |
| 2 | No outputs to extract |
| 3 | Output directory creation failed |

## Notes

- **Read-only operation:** Never modifies the source notebook
- **Base64 decoding:** Automatically decodes embedded images
- **DataFrame handling:** Saves pandas DataFrames as HTML tables
- **Overwrites existing:** Files in output directory may be overwritten
- **Empty cells skipped:** Cells without outputs are ignored

## Common Use Cases

### Extract All Plots
```bash
nbctl extract analysis.ipynb --images
```

### Extract Data Tables
```bash
nbctl extract results.ipynb --data
```

### Custom Output Location
```bash
nbctl extract notebook.ipynb -o ./figures/
```

### Extract Everything
```bash
nbctl extract notebook.ipynb --all
```

## Related Commands

- [`export`](export.md) - Export entire notebook to different formats
- [`run`](run.md) - Execute notebook to generate outputs
- [`clean`](clean.md) - Remove outputs from notebook

## See Also

- [Examples](../examples/extract.md) - Practical usage examples
- [Getting Started](../getting-started/welcome.md) - Introduction to nbctl

