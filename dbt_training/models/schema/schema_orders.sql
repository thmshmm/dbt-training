{{
	config(
		materialized = 'view'
	)
}}

select
	id,
	user_id,
	{{ parse_date('order_date') }} as order_date,
	status
from {{ source('main', 'raw_orders') }}
