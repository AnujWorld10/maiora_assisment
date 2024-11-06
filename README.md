# Sales ETL Pipeline

This project implements an ETL (Extract, Transform, Load) pipeline that processes sales data from two different CSV files (`order_region_a.csv` and `order_region_b.csv`). The data is extracted, transformed according to specified business rules, and loaded into a MySQL database. Additionally, SQL queries are provided for data validation.

## Table of Contents
- Prerequisites
- Project Setup
- Database Setup
- ETL Pipeline
- Data Validation
- File Structure
- Assumptions

---

## Prerequisites

- Python 3.7+
- MySQL Database
- Required Python packages (installed in a virtual environment)

## Project Setup

1. **Clone the repository**:
   ```
   git clone <your-repository-url>
   cd sales_etl
   ```

2. **Create a virtual environment**:
   ```
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

## Database Setup

1. **MySQL Database Configuration**:
   Ensure you have a MySQL server running, and create a database named `maiora_assessment` (or adjust the `DATABASE_URL` in `database.py` as needed).

   ```sql
   CREATE DATABASE maiora_assessment;
   ```

2. **Update Database Credentials**:
   In `database.py`, set the `DATABASE_URL` to match your MySQL credentials:
   ```python
   DATABASE_URL = 'mysql+mysqlconnector://<username>:<password>@localhost/maiora_assessment'
   ```

3. **Run Initial Table Setup**:
   The ETL pipeline will automatically create the required `sales_data` table in the database when run.

## ETL Pipeline

The pipeline consists of three main stages:
1. **Extract**: Reads sales data from two CSV files (`order_region_a.csv` and `order_region_b.csv`).
2. **Transform**: Applies business rules, including:
   - Calculating `total_sales` as `QuantityOrdered * ItemPrice`.
   - Adding a `region` identifier for data from each file.
   - Removing duplicates based on `OrderId`.
   - Adding `net_sale`, calculated as `total_sales - PromotionDiscount`.
   - Filtering out entries with non-positive `net_sale`.
3. **Load**: Loads the transformed data into the `sales_data` table in the MySQL database.

## Running the ETL Process

Run the `main.py` script to execute the ETL process:

```bash
python main.py
```

This will read the data, apply transformations, and load it into the MySQL database. You should see confirmation messages if the process completes successfully.

## Data Validation

After running the ETL process, use the validation functions in `validation.py` to verify data quality and completeness:

- **Total Record Count**: `count_records()` – Counts the total records in the `sales_data` table.
- **Total Sales by Region**: `total_sales_by_region(region)` – Summarizes total sales for a given region (`A` or `B`).
- **Average Sales Amount**: `average_sales_amount()` – Calculates the average sales amount across all records.
- **Duplicate Check**: `check_duplicates()` – Identifies any duplicate `OrderId` values.

## File Structure

```
sales_etl/
├── database.py          # Database setup and connection
├── extract.py           # Extract function to read CSV data
├── load.py              # Load function to insert data into MySQL
├── main.py              # Main ETL pipeline script
├── model.py             # Database model for sales_data table
├── transform.py         # Transformation logic
├── validation.py        # Validation functions for data checks
├── order_region_a.csv   # Sample sales data for region A
├── order_region_b.csv   # Sample sales data for region B
└── README.md            # Project documentation
```

## Assumptions

- The `order_region_a.csv` and `order_region_b.csv` files contain consistent column headers as expected in the assignment.
- The MySQL database and table names are pre-configured according to the instructions.
- `PromotionDiscount` values, if missing, are assumed to be zero.

---

## Additional Notes

Ensure the necessary MySQL user permissions are granted for accessing and modifying the database.

---