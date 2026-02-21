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

seed-data:
	dbt seed

create-manifest:
	dbt compile

start-airflow:
	AIRFLOW_HOME={{invocation_directory()}}/airflow \
	AIRFLOW__CORE__DAGS_FOLDER={{invocation_directory()}}/airflow/dags \
	AIRFLOW__LOGGING__BASE_LOG_FOLDER={{invocation_directory()}}/airflow/logs \
	AIRFLOW__LOGGING__DAG_PROCESSOR_CHILD_PROCESS_LOG_DIRECTORY={{invocation_directory()}}/airflow/logs/dag_processor \
	AIRFLOW__CORE__PLUGINS_FOLDER={{invocation_directory()}}/airflow/plugins \
	AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=sqlite:///{{invocation_directory()}}/airflow/airflow.db \
		airflow standalone
