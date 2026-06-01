# Dom16S: Dominant Organism Identification from 16S Sequencing Data

Dom16S is a Python script designed to process **16S sequencing abundance TSV files** from multiple sample groups and identify **dominant organisms** based on abundance and prevalence across samples.

The script calculates:

- **Total abundance** of each species across samples
- **Prevalence** (number of samples containing the species)
- **Group abundance**
- **Actual abundance**
- **Normalized actual abundance**

This helps identify dominant microbial taxa within experimental groups.

---

## Features

✔ Processes multiple sample groups automatically  
✔ Reads all `.tsv` files inside group folders  
✔ Calculates prevalence-adjusted abundance  
✔ Normalizes abundance across organisms  
✔ Outputs ranked dominant organisms for each group  
✔ Suitable for microbiome and 16S amplicon sequencing studies

---

## Directory Structure

The input directory should contain subfolders representing different groups.

Example:

```text
input_directory/
│── Healthy/
│   ├── sample1.tsv
│   ├── sample2.tsv
│   └── sample3.tsv
│
│── Diseased/
│   ├── sample1.tsv
│   ├── sample2.tsv
│   └── sample3.tsv
```

Each subfolder represents a biological or experimental group.

---

## Input File Format

Each `.tsv` file should contain at least the following columns:

| Column | Description |
|---------|-------------|
| species | Taxonomic species name |
| abundance | Relative abundance/count |

Example:

```tsv
species	abundance
Escherichia coli	25.4
Klebsiella pneumoniae	18.2
Staphylococcus aureus	7.8
```

---

## Calculation Workflow

For each species:

### 1. Total Abundance

The sum of abundance values across all samples.

### 2. Prevalence

The number of unique samples in which the species is present.

### 3. Group Abundance

{Group Abundance} = {Total Abundance} / {Total Samples}

### 4. Actual Abundance

{Actual Abundance} = {Group Abundance} * {Prevalence}

### 5. Normalized Actual Abundance

{Normalized Actual Abundance} = {Actual Abundance} / {Actual Abundance}}

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Dom16S.git
cd Dom16S
```

Install dependencies:

```bash
pip install pandas
```

---

## Requirements

- Python ≥ 3.8
- pandas

---

## Usage

Run the script using:

```bash
python Dom16S.py input_directory
```

Example:

```bash
python Dom16S.py microbiome_groups/
```

---

## Output

For each group, the script generates:

```text
<GroupName>_dominant_organisms.csv
```

Example:

```text
Healthy_dominant_organisms.csv
Diseased_dominant_organisms.csv
```

The output file contains:

| Column | Description |
|---------|-------------|
| species | Species name |
| total_abundance | Sum abundance across samples |
| prevalence | Number of samples containing species |
| group_abundance | Mean abundance in group |
| actual_abundance | Prevalence-adjusted abundance |
| normalized_actual_abundance | Final normalized abundance |

---

## Example Output

| species | total_abundance | prevalence | normalized_actual_abundance |
|----------|----------------|------------|-----------------------------|
| Escherichia coli | 145.3 | 8 | 0.31 |
| Klebsiella pneumoniae | 110.2 | 6 | 0.22 |
| Staphylococcus aureus | 75.1 | 4 | 0.14 |

---

## How It Works

1. Reads all `.tsv` files inside each group folder  
2. Combines sample-level abundance tables  
3. Calculates abundance and prevalence metrics  
4. Computes normalized abundance  
5. Ranks dominant organisms  
6. Saves results as CSV files

---

## Example Command

```bash
python Dom16S.py /path/to/16S_data
```

---

## Citation

If you use this script in your research, please cite the corresponding study or repository.



## License

MIT License
