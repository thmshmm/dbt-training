
{{
    config(
        materialized='ephemeral'
    )
}}

select 
    date_string,
    {{ parse_date('date_string') }} as parsed_date
from (
    select '20240101' as date_string
)