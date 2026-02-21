import marimo

__generated_with = "0.19.11"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import duckdb

    conn = duckdb.connect('data/db.duckdb')
    return conn, mo


@app.cell
def _(conn, mo):
    _df = mo.sql(
        f"""
        SHOW TABLES;
        """,
        engine=conn
    )
    return


@app.cell
def _(conn, mo):
    _df = mo.sql(
        f"""
        SELECT * FROM main.my_first_dbt_model;
        """,
        engine=conn
    )
    return


if __name__ == "__main__":
    app.run()
