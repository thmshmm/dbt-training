import polars as pl


def model(dbt, session):
    # dbt.ref() returns a DuckDB relation which can be converted e.g., to Polars
    orders_df = dbt.ref("orders").pl()

    return orders_df.with_columns([(pl.col("amount") * 2).alias("extended_col")])
