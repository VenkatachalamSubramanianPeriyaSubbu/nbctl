# Combine Command Examples

Practical examples for concatenating notebooks.

## Basic Usage

### Append Two Notebooks

```bash
nbutils combine notebook1.ipynb notebook2.ipynb -o combined.ipynb
```

### With Report

```bash
nbutils combine notebook1.ipynb notebook2.ipynb -o combined.ipynb --report
```

## Strategy Examples

### Append Strategy (Default)

```bash
# Concatenate all cells
nbutils combine intro.ipynb analysis.ipynb -o full.ipynb --strategy append
```

### Keep First Only

```bash
# Copy first notebook (ignore second)
nbutils combine keep.ipynb ignore.ipynb -o output.ipynb --strategy first
```

### Keep Second Only

```bash
# Copy second notebook (ignore first)
nbutils combine ignore.ipynb keep.ipynb -o output.ipynb --strategy second
```

## Workflow Examples

### Build Complete Analysis

```bash
#!/bin/bash
# Combine multiple analysis steps

nbutils combine \
    01_introduction.ipynb \
    02_data_loading.ipynb \
    -o temp1.ipynb

nbutils combine \
    temp1.ipynb \
    03_analysis.ipynb \
    -o temp2.ipynb

nbutils combine \
    temp2.ipynb \
    04_conclusions.ipynb \
    -o complete_analysis.ipynb

rm temp*.ipynb
echo "Complete analysis created"
```

### Create Tutorial

```bash
#!/bin/bash
# Combine lessons into complete tutorial

lessons=(
    "lesson1_basics.ipynb"
    "lesson2_intermediate.ipynb"
    "lesson3_advanced.ipynb"
)

output="complete_tutorial.ipynb"
cp "${lessons[0]}" "$output"

for ((i=1; i<${#lessons[@]}; i++)); do
    temp=$(mktemp)
    nbutils combine "$output" "${lessons[$i]}" -o "$temp"
    mv "$temp" "$output"
done

echo "Tutorial created: $output"
```

### Weekly Report

```bash
#!/bin/bash
# Combine daily analyses into weekly report

week=$(date +%Y-W%U)
output="weekly_report_$week.ipynb"

# Start with header notebook
cp report_header.ipynb "$output"

# Add each day's analysis
for day in mon tue wed thu fri; do
    if [ -f "analysis_${day}.ipynb" ]; then
        temp=$(mktemp)
        nbutils combine "$output" "analysis_${day}.ipynb" -o "$temp"
        mv "$temp" "$output"
    fi
done

echo "Weekly report: $output"
```

## Advanced Examples

### Combine with Separators

```bash
#!/bin/bash
# Add separator notebooks between sections

# Create separator
cat > separator.ipynb << EOF
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["---\n", "\n", "## Next Section\n"]
  }
 ],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 4
}
EOF

# Combine with separators
nbutils combine part1.ipynb separator.ipynb -o temp1.ipynb
nbutils combine temp1.ipynb part2.ipynb -o temp2.ipynb
nbutils combine temp2.ipynb separator.ipynb -o temp3.ipynb
nbutils combine temp3.ipynb part3.ipynb -o complete.ipynb

rm temp*.ipynb separator.ipynb
```

### Conditional Combining

```bash
#!/bin/bash
# Combine notebooks if they exist

notebooks=(
    "intro.ipynb"
    "analysis.ipynb"
    "conclusion.ipynb"
)

# Start with first notebook
output="combined.ipynb"
first=true

for nb in "${notebooks[@]}"; do
    if [ ! -f "$nb" ]; then
        echo "⚠ Skipping missing: $nb"
        continue
    fi
    
    if $first; then
        cp "$nb" "$output"
        first=false
    else
        temp=$(mktemp)
        nbutils combine "$output" "$nb" -o "$temp"
        mv "$temp" "$output"
    fi
done

echo "Combined notebooks: $output"
```

### Archive Multiple Versions

```bash
#!/bin/bash
# Combine and archive different versions

versions=("v1" "v2" "v3")

for ver in "${versions[@]}"; do
    output="analysis_${ver}_complete.ipynb"
    nbutils combine \
        "analysis_${ver}_part1.ipynb" \
        "analysis_${ver}_part2.ipynb" \
        -o "$output" \
        --report
done
```

## Batch Operations

### Combine All in Directory

```bash
#!/bin/bash
# Combine all notebooks in order

output="all_combined.ipynb"
first=true

for nb in *.ipynb | sort; do
    if $first; then
        cp "$nb" "$output"
        first=false
    else
        temp=$(mktemp)
        nbutils combine "$output" "$nb" -o "$temp"
        mv "$temp" "$output"
    fi
done
```

### Combine by Pattern

```bash
#!/bin/bash
# Combine notebooks matching pattern

# Combine all analysis notebooks
nbutils combine analysis_*.ipynb --order -o all_analysis.ipynb

# Combine all model notebooks
nbutils combine model_*.ipynb --order -o all_models.ipynb
```

## Team Collaboration

### Merge Team Contributions

```bash
#!/bin/bash
# Combine work from team members

members=("alice" "bob" "charlie")
output="team_analysis.ipynb"

# Start with template
cp template.ipynb "$output"

for member in "${members[@]}"; do
    nb="${member}_contribution.ipynb"
    if [ -f "$nb" ]; then
        temp=$(mktemp)
        nbutils combine "$output" "$nb" -o "$temp" --report
        mv "$temp" "$output"
        echo "Added $member's contribution"
    fi
done

echo "Team analysis complete: $output"
```

## Tips & Best Practices

### 1. Clean Before Combining

```bash
# Clean notebooks first
nbutils clean notebook1.ipynb
nbutils clean notebook2.ipynb

# Then combine
nbutils combine notebook1.ipynb notebook2.ipynb -o combined.ipynb
```

### 2. Add Headers

Add markdown headers to separate sections:

```bash
# In notebook1, add final cell:
## End of Part 1

# In notebook2, add first cell:
## Part 2
```

### 3. Verify Result

```bash
# Combine
nbutils combine nb1.ipynb nb2.ipynb -o combined.ipynb

# Verify
nbutils info combined.ipynb
```

### 4. Use Reports

```bash
# Always use --report for complex combinations
nbutils combine nb1.ipynb nb2.ipynb -o combined.ipynb --report
```

## Related Examples

- [Resolve Examples](resolve.md) - Intelligent merging
- [Diff Examples](diff.md) - Compare notebooks
- [Clean Examples](clean.md) - Clean before combining

