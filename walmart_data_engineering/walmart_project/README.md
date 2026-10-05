# 🛒 Walmart-Inspired Data Engineering Pipeline

An end-to-end **retail data engineering project** built using **Databricks, dbt, Apache Airflow, Python, SQL, Docker, and Git**.

The project demonstrates how raw retail data can be transformed into reliable, analytics-ready datasets using a modern **Lakehouse + ELT architecture**.

> **Note:** This is a personal Walmart-inspired project created for learning and portfolio purposes. It is not an official Walmart project.

---

## 🏗️ Architecture

```text
              Raw Data
                  │
                  ▼
          ┌───────────────┐
          │  Databricks   │
          │   Lakehouse   │
          └───────┬───────┘
                  │
                  ▼
             ┌─────────┐
             │   dbt   │
             │         │
             │Transform│
             │  Test   │
             │Snapshot │
             └────┬────┘
                  │
                  ▼
          ┌───────────────┐
          │   Gold Layer  │
          │               │
          │ Fact + Dim    │
          │   Models      │
          └───────────────┘

        ┌───────────────────┐
        │   Apache Airflow  │
        │   Orchestration   │
        └───────────────────┘
```

---

## 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| **Databricks** | Lakehouse & data processing |
| **dbt** | SQL transformation, testing & snapshots |
| **Apache Airflow** | Workflow orchestration |
| **Python** | Pipeline utilities |
| **SQL** | Data transformation & modeling |
| **Docker** | Containerized Airflow environment |
| **Git/GitHub** | Version control |

---

## 🔄 Pipeline

### 1. Data Ingestion

Raw retail data is loaded into Databricks for processing.

The pipeline demonstrates:

- Incremental ingestion
- Metadata-driven processing
- Structured data processing

### 2. Medallion Architecture

```text
Bronze
  ↓
Silver
  ↓
Gold
```

**Bronze** → Raw data  
**Silver** → Cleaned and transformed data  
**Gold** → Analytics-ready data

### 3. dbt Transformations

dbt is used for modular SQL transformations including:

- Staging models
- Silver models
- Incremental models
- Ephemeral models
- Business transformations

### 4. Data Quality

Implemented dbt tests such as:

- `not_null`
- `unique`
- `accepted_values`
- Custom SQL tests

Example:

```yaml
columns:
  - name: customer_id
    tests:
      - unique
      - not_null
```

### 5. Historical Data — SCD Type 2

dbt snapshots are used to track changes to business entities over time.

```text
Customer 101

Mumbai
  ↓
Pune
```

Instead of overwriting the previous value, historical versions are maintained.

### 6. Data Modeling

The Gold layer uses dimensional modeling concepts including:

- Fact tables
- Dimension tables
- Star schema
- One Big Table (OBT)

```text
             dim_customer
                   │
                   ▼
dim_product ──► fact_orders ◄── dim_store
                   │
                   ▼
                dim_date
```

### 7. Airflow Orchestration

Apache Airflow coordinates the pipeline:

```text
Ingestion
    ↓
Databricks Processing
    ↓
dbt Transformation
    ↓
Data Quality Tests
    ↓
Snapshots
    ↓
Gold Models
```

Airflow handles scheduling, dependencies, retries, and workflow execution.

---

## 🎯 Key Data Engineering Concepts

- Lakehouse Architecture
- Medallion Architecture
- ELT
- Incremental Processing
- Metadata-Driven Pipelines
- dbt Models
- dbt Testing
- dbt Snapshots
- SCD Type 2
- Star Schema
- Fact & Dimension Modeling
- One Big Table
- Workflow Orchestration
- Dockerized Airflow

---

## 📂 Project Structure

```text
walmart-data-engineering/
│
├── airflow/
│   └── dags/
│
├── dbt/
│   └── walmart_dbt/
│       ├── models/
│       │   ├── staging/
│       │   ├── silver/
│       │   └── gold/
│       ├── snapshots/
│       ├── tests/
│       └── dbt_project.yml
│
├── databricks/
│   └── notebooks/
│
├── docker/
│
├── scripts/
│
├── .gitignore
└── README.md
```

*Update the structure to match your actual repository.*

---

## 🧪 Data Quality

The pipeline validates data before it reaches analytical models.

```text
Raw Data
   ↓
Transformation
   ↓
dbt Tests
   ↓
     ├── PASS → Gold Layer
     │
     └── FAIL → Pipeline Failure
```

---

## ⚙️ Setup

### Prerequisites

- Python
- Git
- Docker
- Databricks
- dbt
- Apache Airflow

### Clone

```bash
git clone https://github.com/<your-username>/walmart-data-engineering.git

cd walmart-data-engineering
```

### Start Airflow

```bash
docker compose up -d
```

Configure your Databricks and local environment credentials before running the pipeline.

---

## 📈 Future Improvements

- CI/CD with GitHub Actions
- Pipeline monitoring & alerting
- Automated documentation
- Data lineage
- Performance optimization
- Infrastructure as Code
- Production deployment

---

