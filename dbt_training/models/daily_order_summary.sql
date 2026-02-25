{{
    config(
        materialized='incremental',
        unique_key='order_date',
        on_schema_change='fail'
    )
}}

select

	order_date,
	count(distinct order_id) as total_orders,

	-- Metadata fields
	current_timestamp as last_updated_at,
	'{{ run_started_at }}' as dbt_run_started_at

from {{ ref('stg_orders') }}

-- INCREMENTAL LOGIC
{% if is_incremental() %}
	where order_date > (select max(order_date) from {{ this }})
{% endif %}

group by 1
