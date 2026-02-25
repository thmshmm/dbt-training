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

    def q(query):
        with duckdb.connect('data/db.duckdb', read_only=True) as conn:
            return conn.sql(query).pl()

    return mo, q


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Examples
    """)
    return


@app.cell
def _(q):
    q("show tables;")
    return


@app.cell
def _(q):
    q("from schema_orders;")
    return


@app.cell
def _(q):
    q("from stg_orders;")
    return


@app.cell
def _(q):
    q("from daily_order_summary;")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Incremental
    """)
    return


@app.cell
def _(q):
    q("""
        select order_date, dbt_run_started_at
        from daily_order_summary 
        order by 1 desc
        limit 10;
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Python model
    """)
    return


@app.cell
def _(q):
    q("""
        select order_date, total_orders, total_orders_doubled
        from orders_extended;
    """)
    return


if __name__ == "__main__":
    app.run()
