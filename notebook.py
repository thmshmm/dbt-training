import marimo

__generated_with = "0.19.11"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Initialize
    """)
    return


@app.cell
def _():
    import marimo as mo
    import duckdb

    conn = duckdb.connect('data/db.duckdb', read_only=True)
    return conn, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Cleanup
    """)
    return


@app.cell
def _(conn):
    conn.close()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Examples
    """)
    return


@app.cell
def _(conn, mo):
    _df = mo.sql(
        f"""
        SHOW TABLES;
        """,
        engine=conn
    )
    return


@app.cell(hide_code=True)
def _(conn, mo):
    _df = mo.sql(
        f"""
        SELECT * FROM main.customers;
        """,
        engine=conn
    )
    return


@app.cell
def _(conn, mo, raw_orders):
    _df = mo.sql(
        f"""
        DESCRIBE FROM raw_orders;
        """,
        engine=conn
    )
    return


@app.cell
def _(conn, mo, orders):
    _df = mo.sql(
        f"""
        DESCRIBE FROM orders;
        """,
        engine=conn
    )
    return


@app.cell
def _(conn, mo, orders):
    _df = mo.sql(
        f"""
        FROM orders;
        """,
        engine=conn
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Incremental
    """)
    return


@app.cell
def _(conn, daily_order_summary, mo):
    _df = mo.sql(
        f"""
        SELECT order_date, dbt_run_started_at
        FROM daily_order_summary 
        ORDER BY 1 DESC
        LIMIT 10;
        """,
        engine=conn
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Python model
    """)
    return


@app.cell
def _(conn, mo, orders_extended):
    _df = mo.sql(
        f"""
        SELECT
            order_id,
            order_date,
            amount,
            extended_col
        FROM orders_extended;
        """,
        engine=conn
    )
    return


if __name__ == "__main__":
    app.run()
