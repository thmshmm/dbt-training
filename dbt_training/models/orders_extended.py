import polars as pl


def model(dbt, session):
    # dbt.ref() returns a DuckDB relation which can be converted e.g., to Polars

    orders_df = dbt.ref("daily_order_summary").pl()

    return orders_df.with_columns([(pl.col("total_orders") * 2).alias("total_orders_doubled")])
