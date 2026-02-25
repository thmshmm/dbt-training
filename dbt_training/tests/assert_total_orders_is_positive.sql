select

    order_date,
    total_orders

from {{ ref('orders_extended') }}

where total_orders < 0