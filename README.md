# Perqara ETL Assessment Project

This project implements an ETL (Extract, Transform, Load) pipeline to process data using Python and DuckDB. The goal is to build a clean, query-ready dataset from raw CSV files.

---

## Data Sources
All source files are stored under the `Source/` directory:
- `customer_details.csv`
- `product_details.csv`
- `E-commerece sales data 2024.csv`

---

## ETL Pipeline Stages

### 1. **Extraction** (`LoadData.py`)
- Loads raw CSV files into pandas DataFrames.
- Displays initial previews.

### 2. **Cleaning** (`CleanData.py`)
- Removes unnamed columns, empty rows, and duplicates from all datasets.

### 3. **Normalization** (`NormalizeData.py`)
- Renames inconsistent columns.
- Converts data types for numeric and datetime consistency.
- Handles missing values.

### 4. **Loading to Database** (`LoadToDuckDB.py`)
- Loads the transformed DataFrames into a DuckDB file (`perqara.duckdb`) as:
  - `customers`
  - `products`
  - `sales`

### 5. **Display Sample Data** (`ShowData.py`)
- Queries and displays top records from each table to confirm successful loading.

---

## How to Run

Ensure you have all the required libraries (mainly `pandas` and `duckdb`), then simply execute:

```bash
python Main.py
```

---

## Output
- A `perqara.duckdb` file with clean, structured tables.
- Terminal preview of top 5 rows from each table.

---

## Technologies Used
- Python 3
- pandas
- DuckDB

---

## Author
**Aina Aji Dian Pertiwi**
