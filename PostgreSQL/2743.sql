SELECT
    name,
    LENGTH(name) as length
FROM people
ORDER BY length DESC
;