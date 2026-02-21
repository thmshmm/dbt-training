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


if __name__ == "__main__":
    app.run()
