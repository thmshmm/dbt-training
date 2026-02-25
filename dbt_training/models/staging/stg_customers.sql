select

    id as customer_id,
    first_name,
    last_name

from {{ source('main', 'raw_customers') }}
