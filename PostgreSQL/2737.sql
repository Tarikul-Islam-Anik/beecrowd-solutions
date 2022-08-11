WITH average_customers AS (
	SELECT 
		'Average' as name,
		CAST(AVG(customers_number) AS integer) as customers_number,
		2 AS order_filter
	FROM lawyers	
)
SELECT
	name,
	customers_number
FROM (
	
	SELECT 
		name,
		customers_number,
		1 AS order_filter
	FROM lawyers
	WHERE customers_number = (SELECT MAX(customers_number) FROM lawyers)
		OR customers_number = (SELECT MIN(customers_number) FROM lawyers)

	UNION ALL (TABLE average_customers) 

) AS lawyers_customers
ORDER BY order_filter, customers_number DESC
;
