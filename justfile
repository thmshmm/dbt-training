export DBT_PROJECT_DIR := "./dbt_training"
export DBT_PROFILES_DIR := "./dbt_training"

cleanup-project:
	rm -rf data/db.duckdb

setup-project:
	mkdir -p data
	duckdb data/db.duckdb "PRAGMA database_size;"

start-duckdb:
	duckdb data/db.duckdb -ui

start-notebook:
	marimo edit notebook.py

start-airflow:
	AIRFLOW_HOME={{invocation_directory()}}/airflow \
	AIRFLOW__CORE__DAGS_FOLDER={{invocation_directory()}}/airflow/dags \
	AIRFLOW__LOGGING__BASE_LOG_FOLDER={{invocation_directory()}}/airflow/logs \
	AIRFLOW__LOGGING__DAG_PROCESSOR_CHILD_PROCESS_LOG_DIRECTORY={{invocation_directory()}}/airflow/logs/dag_processor \
	AIRFLOW__CORE__PLUGINS_FOLDER={{invocation_directory()}}/airflow/plugins \
	AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=sqlite:///{{invocation_directory()}}/airflow/airflow.db \
		airflow standalone

seed-data:
	dbt seed

create-manifest:
	dbt compile

# Run the incremental model example 
run-incremental:
	dbt run --select daily_order_summary

# Run incremental model with full refresh (rebuilds from scratch)
run-incremental-full:
	dbt run --select daily_order_summary --full-refresh

# Add test data with future dates to demonstrate incremental processing
add-test-data:
	@echo "100,1,20180501,completed" >> dbt_training/seeds/raw_orders.csv
	@echo "101,2,20180502,completed" >> dbt_training/seeds/raw_orders.csv  
	@echo "102,3,20180503,placed" >> dbt_training/seeds/raw_orders.csv
	dbt seed --select raw_orders
	@echo "New test data added! Now run 'just run-incremental' to see incremental processing."

# Build all models including the incremental example
build-all:
	dbt build

run-unit-tests:
	dbt test --select test_type:unit

dbt-docs:
	dbt docs generate
	dbt docs serve