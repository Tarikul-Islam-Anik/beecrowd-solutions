SELECT SUBSTR(natural_person.cpf, 1, 3) || '.' ||
	   SUBSTR(natural_person.cpf, 4, 3) || '.' ||
	   SUBSTR(natural_person.cpf, 7, 3) || '-' ||
	   SUBSTR(natural_person.cpf, 10, 2) AS cpf
FROM natural_person
INNER JOIN customers
    ON natural_person.id_customers = customers.id
;