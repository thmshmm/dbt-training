with source as (

    select * from {{ ref('schema_orders') }}

),

renamed as (

    select

        id as order_id,
        user_id as customer_id,

        -- Call a macro
        {{ parse_date('order_date') }} as order_date,

        status

    from source

)

select * from renamed
