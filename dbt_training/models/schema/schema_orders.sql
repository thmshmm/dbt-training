{{
	config(
		materialized = 'view'
	)
}}

select
	id,
	user_id,
    cast(strptime(cast(order_date as varchar), '%Y%m%d') as date) as order_date,
	-- {{ parse_date('order_date') }} as order_date,
	status
from {{ source('main', 'raw_orders') }}
