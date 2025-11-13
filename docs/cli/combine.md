# nbctl combine

Concatenate or combine two notebooks.

## Description

The `combine` command merges two Jupyter notebooks into one. It supports multiple strategies for combining notebooks, from simple concatenation to selective merging. This is useful for joining analyses, combining work from multiple notebooks, or creating comprehensive reports.

Use this command to:
- Concatenate multiple analyses into one
- Merge notebook sections
- Create comprehensive reports
- Combine work from team members
- Build composite notebooks

## Usage

```bash
nbctl combine NOTEBOOK1 NOTEBOOK2 --output OUTPUT [OPTIONS]
```

## Arguments

| Argument | Description | Required |
|----------|-------------|----------|
| `NOTEBOOK1` | Path to first notebook | Yes |
| `NOTEBOOK2` | Path to second notebook | Yes |

## Options

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `--output` | `-o` | PATH | Required | Output file path for combined notebook |
| `--strategy` | | TEXT | `append` | Combine strategy: `append`, `first`, `second` |
| `--report` | | Flag | False | Show detailed combination report |

## Combine Strategies

### 1. Append (Default)

Concatenates all cells from both notebooks in order:

```
NOTEBOOK1 cells → NOTEBOOK2 cells → OUTPUT
```

**Result:**
```
notebook1 cell 1
notebook1 cell 2
notebook1 cell 3
notebook2 cell 1
notebook2 cell 2
→ combined.ipynb
```

**Use case:** Joining sequential analyses, building reports

---

### 2. First

Keeps only the first notebook (essentially a copy):

```
NOTEBOOK1 cells → OUTPUT
```

**Result:**
```
notebook1 cell 1
notebook1 cell 2
notebook1 cell 3
→ combined.ipynb (notebook2 ignored)
```

**Use case:** Using combine syntax but selecting one notebook

---

### 3. Second

Keeps only the second notebook (essentially a copy):

```
NOTEBOOK2 cells → OUTPUT
```

**Result:**
```
notebook2 cell 1
notebook2 cell 2
→ combined.ipynb (notebook1 ignored)
```

**Use case:** Using combine syntax but selecting one notebook

## Output

### Default Output

```
Notebooks combined successfully

Strategy: append
Output: combined.ipynb

Summary:
  - Cells from notebook1.ipynb: 15
  - Cells from notebook2.ipynb: 12
  - Total cells in output: 27
```

### With Report (`--report`)

```
Notebooks combined successfully

Detailed Report:

Input Notebooks:
  notebook1.ipynb
    - Total cells: 15
    - Code cells: 10
    - Markdown cells: 5
    - Size: 45.2 KB

  notebook2.ipynb
    - Total cells: 12
    - Code cells: 8
    - Markdown cells: 4
    - Size: 32.1 KB

Strategy: append

Output Notebook:
  combined.ipynb
    - Total cells: 27
    - Code cells: 18
    - Markdown cells: 9
    - Size: 77.3 KB

Cell Order:
  Cells 0-14: From notebook1.ipynb
  Cells 15-26: From notebook2.ipynb
```

## Output Structure

The combined notebook preserves:

- Cell content (source code, markdown)
- Cell types (code, markdown, raw)
- Cell outputs (if present)
- Execution counts (if present)
- Cell metadata

Notebook metadata:
- Uses metadata from first notebook (language, kernel, etc.)

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success, notebooks combined |
| 1 | Files not found or invalid notebooks |
| 2 | Output file error |
| 3 | Invalid strategy specified |

## Examples of Use Cases

### Sequential Analysis

Combine data loading and analysis:

```bash
nbctl combine 01_load_data.ipynb 02_analyze.ipynb -o full_analysis.ipynb
```

---

### Build Report

Combine multiple analysis sections:

```bash
# Combine intro + analysis + conclusion
nbctl combine intro.ipynb analysis.ipynb -o temp.ipynb
nbctl combine temp.ipynb conclusion.ipynb -o report.ipynb
```

---

### Merge Team Work

Combine notebooks from different team members:

```bash
nbctl combine alice_work.ipynb bob_work.ipynb -o team_analysis.ipynb
```

---

### Create Tutorial

Combine multiple teaching notebooks:

```bash
nbctl combine lesson1.ipynb lesson2.ipynb -o complete_tutorial.ipynb
```

## Comparison with resolve

| Command | Purpose | Conflict Detection | Use Case |
|---------|---------|-------------------|----------|
| **combine** | Concatenate notebooks | No | Sequential joining |
| **resolve** | 3-way merge | Yes | Merge conflicts, git integration |

**When to use:**

- **combine:** Simple concatenation, building reports, sequential analyses
- **resolve:** Merging branches, resolving git conflicts, intelligent merging

## Notes

- **Read-only:** Never modifies input notebooks
- **Order matters:** notebook1 comes before notebook2 in output
- **Metadata:** Uses metadata from first notebook
- **Cell IDs:** May regenerate cell IDs in output
- **Outputs preserved:** Cell outputs are kept if present
- **Multiple combinations:** Can chain combines for >2 notebooks

## Chaining Combinations

To combine more than 2 notebooks:

```bash
# Method 1: Chain commands
nbctl combine nb1.ipynb nb2.ipynb -o temp1.ipynb
nbctl combine temp1.ipynb nb3.ipynb -o temp2.ipynb
nbctl combine temp2.ipynb nb4.ipynb -o final.ipynb

# Method 2: Script it
notebooks=("nb1.ipynb" "nb2.ipynb" "nb3.ipynb" "nb4.ipynb")
output="combined.ipynb"
cp "${notebooks[0]}" "$output"
for ((i=1; i<${#notebooks[@]}; i++)); do
    nbctl combine "$output" "${notebooks[$i]}" -o temp.ipynb
    mv temp.ipynb "$output"
done
```

## Best Practices

### 1. Clear Separation

Add markdown headers between sections:

```bash
# In notebook1, add final cell:
## End of Part 1

# In notebook2, add first cell:
## Part 2: Analysis
```

### 2. Clean Before Combining

```bash
# Clean notebooks first
nbctl clean notebook1.ipynb
nbctl clean notebook2.ipynb

# Then combine
nbctl combine notebook1.ipynb notebook2.ipynb -o combined.ipynb
```

### 3. Check Before Combining

```bash
# Review notebooks first
nbctl info notebook1.ipynb
nbctl info notebook2.ipynb

# Then combine
nbctl combine notebook1.ipynb notebook2.ipynb -o combined.ipynb
```

### 4. Verify Output

```bash
# Combine
nbctl combine nb1.ipynb nb2.ipynb -o combined.ipynb

# Verify
nbctl info combined.ipynb
```

## Limitations

- **No conflict detection:** Simply concatenates, doesn't detect conflicts
- **No intelligent merging:** Doesn't merge similar cells
- **Linear combination:** Only combines two notebooks at a time
- **Metadata from first:** Uses first notebook's metadata
- **No deduplication:** Doesn't remove duplicate cells

For intelligent merging with conflict detection, use [`resolve`](resolve.md).

## Related Commands

- [`resolve`](resolve.md) - Intelligent 3-way merge with conflict detection
- [`diff`](diff.md) - Compare notebooks before combining
- [`clean`](clean.md) - Clean notebooks before combining
- [`info`](info.md) - Analyze notebooks before combining

## See Also

- [Examples](../examples/combine.md) - Practical usage examples
- [Getting Started](../getting-started/welcome.md) - Introduction to nbctl

