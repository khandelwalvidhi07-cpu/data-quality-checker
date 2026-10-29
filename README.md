
# Data Quality Checker

A beginner-friendly Python project that checks customer CSV files for common data-quality issues.

## Features

- Reads customer data from a CSV file.
- Detects missing values in each column.
- Identifies duplicate rows.
- Counts rows affected by one or more issues.
- Prints a data quality report.
- Saves the report to `quality_report.txt`.
- Handles basic file errors.
- Does not modify the original CSV file.

## Technologies

- Python
- csv module
- Dictionaries, lists, loops, functions, and sets

## How to Run

1. Install Python.
2. Download or clone this repository.
3. Open the project folder in a terminal.
4. Run:

   ```bash
   python main.py
   ```

## Project Files

- `main.py` — Main program.
- `customers.csv` — Sample customer data.
- `quality_report.txt` — Generated report.

## Limitations

This version checks for missing values and completely identical rows. It does not yet validate email formats or detect records with matching customer IDs but different information.

## Learning Goal

This project was built to practise Python file handling, CSV processing, functions, loops, dictionaries, sets, and basic error handling.
