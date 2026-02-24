# dbt Training Project

This is an example project for teaching the basics of dbt (data build tool). It includes:

- **Local Airflow instance** for orchestration
- **DuckDB** as the database (lightweight and file-based)
- **Jaffle Shop example** from dbt (customers, orders, payments)
- **Incremental model example** to showcase advanced materialization patterns

## Quick Start

This project uses [just](https://github.com/casey/just) as a command runner. All commands should be run from the project root.

Ensure you have `just` and `duckdb` installed on your machine before proceeding.

### Initial Setup

```bash
# Set up the project and database
just setup-project

# Source the .envrc or use direnv to activate the virtual environment and set required environment variables
source .envrc

# Load initial seed data
just seed-data

# Build all models
just build-all
```

### Running Models

```bash
# Build all models
just build-all

# Run just the incremental model
just run-incremental

# Run incremental model with full refresh (rebuilds from scratch)
just run-incremental-full
```

### Exploring Data

```bash
# Start DuckDB with UI to explore data
just start-duckdb

# Start Marimo notebook for interactive analysis
just start-notebook
```

### Airflow Integration

```bash
# Start Airflow standalone mode
just start-airflow
```

## Project Structure

```
├── dbt_training/          # dbt project directory
│   ├── models/            # dbt models
│   │   ├── staging/       # Staging layer models
│   │   ├── unit_tests/    # Ephemeral models for unit tests
│   │   ├── daily_order_summary.sql  # Incremental model example
│   │   └── ...
│   ├── seeds/             # CSV files for initial data, used to simulate sources
│   ├── macros/            # Reusable logic macros
│   └── tests/             # Data quality tests
├── airflow/               # Airflow DAGs and configuration
├── data/                  # DuckDB database file
└── justfile               # Command automation
```

## Environment Variables

The project uses these environment variables (automatically set by just):
- `DBT_PROJECT_DIR=./dbt_training`
- `DBT_PROFILES_DIR=./dbt_training`
