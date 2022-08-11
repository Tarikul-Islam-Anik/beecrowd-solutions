SELECT
    customers.name,
    rentals.rentals_date
FROM rentals
INNER JOIN customers
    ON rentals.id_customers = customers.id
WHERE rentals.rentals_date >= '2016-09-01' 
	AND rentals.rentals_date < '2016-10-01'
	;
