SELECT customers.name
FROM legal_person
INNER JOIN customers
    ON legal_person.id_customers = customers.id
;
