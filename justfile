export DBT_PROJECT_DIR := "./dbt_training"
export DBT_PROFILES_DIR := "./dbt_training"

cleanup-project:
	rm -rf data/db.duckdb

setup-project:
	mkdir -p data
	duckdb data/db.duckdb "PRAGMA database_size;"

build-examples:
	dbt build --select example

start-duckdb:
	duckdb data/db.duckdb -ui

start-notebook:
	marimo edit notebook.py
