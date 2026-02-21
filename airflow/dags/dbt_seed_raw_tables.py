from datetime import datetime
from pathlib import Path

from airflow.sdk import dag, task

PROJECT_ROOT = str(Path(__file__).resolve().parents[2].absolute())


@task.bash(cwd=PROJECT_ROOT)
def run_dbt() -> str:
    return """
        DBT_PROJECT_DIR="./dbt_training" \
        DBT_PROFILES_DIR="./dbt_training" \
            dbt seed
        """


@dag(schedule=None, start_date=datetime(2026, 1, 1), catchup=False)
def dbt_seed_raw_tables():
    run_dbt()


dbt_seed_raw_tables()
