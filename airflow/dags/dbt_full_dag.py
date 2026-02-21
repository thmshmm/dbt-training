import datetime
import json
from pathlib import Path

from airflow.sdk import dag, task
from airflow.sdk.bases.decorator import Task

PROJECT_ROOT = str(Path(__file__).resolve().parents[2].absolute())


def load_manifest():
    local_filepath = f"{PROJECT_ROOT}/dbt_training/target/manifest.json"
    with open(local_filepath) as f:
        data = json.load(f)

    return data


@task.bash(cwd=PROJECT_ROOT)
def run_dbt(model: str) -> str:
    return """
        DBT_PROJECT_DIR="./dbt_training" \
        DBT_PROFILES_DIR="./dbt_training" \
            dbt build --select {0}
        """.format(model)


def run_dbt_with_id(id: str) -> Task:
    return run_dbt.override(task_id=id)


# Limited to 1 active task because DuckDB doesn't support multiple concurrent connections.
@dag(
    schedule=None,
    start_date=datetime.datetime(2026, 1, 1),
    catchup=False,
    max_active_tasks=1,
)
def dbt_full_dag():
    data = load_manifest()

    dbt_tasks = {}

    for node in data["nodes"].keys():
        if node.split(".")[0] == "model":
            model = node.split(".")[-1]
            dbt_tasks[node] = run_dbt_with_id(node)(model)

    for node in data["nodes"].keys():
        if node.split(".")[0] == "model":
            for upstream_node in data["nodes"][node]["depends_on"]["nodes"]:
                upstream_node_type = upstream_node.split(".")[0]
                if upstream_node_type == "model":
                    dbt_tasks[upstream_node] >> dbt_tasks[node]


dbt_full_dag()
