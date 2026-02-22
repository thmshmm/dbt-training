{{
    config(
        materialized='incremental',
        unique_key='order_date',
        on_schema_change='fail'
    )
}}

with orders_with_payments as (

    select 
        o.order_date,
        o.order_id,
        o.customer_id,
        o.status,
        p.amount as payment_amount,
        p.payment_method
    from {{ ref('stg_orders') }} o
    left join {{ ref('stg_payments') }} p
        on o.order_id = p.order_id

),

daily_metrics as (

    select
        order_date,

        count(distinct order_id) as total_orders,
        count(distinct case when status = 'completed' then order_id end) as completed_orders,
        count(distinct case when status = 'returned' then order_id end) as returned_orders,
        count(distinct case when status = 'placed' then order_id end) as placed_orders,
        count(distinct case when status = 'shipped' then order_id end) as shipped_orders,

        -- Metadata fields
        current_timestamp as last_updated_at,
        '{{ run_started_at }}' as dbt_run_started_at

    from orders_with_payments
    
    -- INCREMENTAL LOGIC
    {% if is_incremental() %}
        where order_date > (select max(order_date) from {{ this }})
    {% endif %}
    
    group by 1

)

select * from daily_metrics