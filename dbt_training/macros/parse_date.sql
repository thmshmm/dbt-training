{% macro parse_date(column_name) %}
    cast(strptime(cast({{ column_name }} as varchar), '%Y%m%d') as date)
{% endmacro %}
