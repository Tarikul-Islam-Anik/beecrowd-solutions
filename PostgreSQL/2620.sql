SELECT
    customers.name,
    orders.id
FROM orders
INNER JOIN customers
    ON orders.id_customers = customers.id
WHERE EXTRACT(MONTH FROM orders.orders_date) BETWEEN 1 AND 6 
	AND EXTRACT(YEAR FROM orders.orders_date) = 2016
;