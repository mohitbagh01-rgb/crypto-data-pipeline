# Crypto Market ETL Pipeline

A modular ETL pipeline built using Python and Pandas that collects real-time cryptocurrency market data from the Zebpay API, cleans and transforms it, and stores it in Parquet format for efficient analytics and future processing.

---

# Project Overview

This project was created to understand how real-world data engineering pipelines work using live API data.

The pipeline follows the complete ETL process:

* **Extract** → Fetch cryptocurrency market data from the Zebpay API
* **Transform** → Clean, validate, and structure the raw JSON data
* **Load** → Store the processed data in Parquet format for analytics workloads

The goal of this project was not just to fetch data, but to build a scalable and modular pipeline similar to what is used in production data systems.

---

# Architecture

```text
           Zebpay API
                │
                ▼
        Ingestion Layer
          (ingest.py)
                │
                ▼
      Transformation Layer
        (transform.py)
                │
                ▼
           Load Layer
           (load.py)
                │
                ▼
        Parquet Data Storage
```

---

# Features

* Real-time cryptocurrency data ingestion using API calls
* Modular ETL pipeline structure
* JSON to Pandas DataFrame conversion
* Missing value and duplicate handling
* Safe datatype conversion for inconsistent API data
* Optimized Parquet file storage
* Fault-tolerant transformation logic
* Git and GitHub integration for version control

---

# Tech Stack

| Technology   | Purpose                          |
| ------------ | -------------------------------- |
| Python       | Core programming language        |
| Pandas       | Data cleaning and transformation |
| Requests     | API handling                     |
| PyArrow      | Parquet file support             |
| Git & GitHub | Version control                  |

---

# Project Structure

```text
crypto-data-pipeline/
│
├── data/
│   ├── raw_data/
│   └── processed_data/
│
├── src/
│   ├── ingest.py
│   ├── transform.py
│   └── load.py
│
├── pipeline.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Pipeline Workflow

## 1. Data Ingestion

The ingestion layer connects to the Zebpay API and fetches live cryptocurrency market data.

Key tasks:

* API request handling
* Response validation
* Exception handling for failed requests

---

## 2. Data Transformation

The raw JSON data is converted into a structured Pandas DataFrame and cleaned for analysis.

Transformation steps include:

* Removing duplicate records
* Handling missing values
* Safe numeric datatype conversion
* Dropping highly sparse or irrelevant columns

Example:

```python
pd.to_numeric(errors="coerce")
```

This helps prevent pipeline failures caused by invalid numeric values.

---

## 3. Data Loading

The cleaned dataset is stored in Parquet format to improve storage efficiency and analytical performance.

---

# Challenges Faced

## Handling Dirty API Data

One of the main challenges was dealing with inconsistent API responses.

Some numeric fields contained:

* Empty strings
* Null values
* Unexpected formats

These issues caused datatype conversion errors during transformation.

### Solution

To make the pipeline fault tolerant:

* Used safe numeric conversion with:

```python
pd.to_numeric(errors="coerce")
```

* Converted invalid values into `NaN`
* Applied missing value handling strategies
* Added data cleaning steps before storage

This made the pipeline much more reliable for real-world data.

---

# Why Parquet?

Parquet is a columnar storage format commonly used in modern data engineering workflows.

### Benefits of using Parquet:

* Better compression
* Faster query performance
* Efficient column-based reads
* Reduced storage usage
* Analytics-friendly structure

---

# How to Run

## Clone Repository

```bash
git clone https://github.com/mohitbagh01-rgb/crypto-data-pipeline.git
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Pipeline

```bash
python pipeline.py
```

---

# Learning Outcomes

This project helped me understand:

* ETL pipeline architecture
* Real-world API data ingestion
* Data cleaning and preprocessing
* Handling semi-structured JSON data
* Managing schema inconsistencies
* Fault-tolerant transformation design
* Efficient storage using Parquet
* Writing modular and maintainable code

---

# Future Improvements

Some improvements planned for future versions:

* Logging and monitoring system
* Schema validation
* PostgreSQL integration
* Apache Airflow scheduling
* Docker containerization
* Automated alerts and monitoring

---

