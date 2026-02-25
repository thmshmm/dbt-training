{{
	config(
		materialized = 'view'
	)
}}

select

	id,
	user_id,
	order_date,
	status

from {{ source('main', 'raw_orders') }}
