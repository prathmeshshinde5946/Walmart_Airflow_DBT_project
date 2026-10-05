select * from {{ source('walmart_databricks', 'products') }};
