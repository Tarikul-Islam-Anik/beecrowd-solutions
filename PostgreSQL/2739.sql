SELECT
    name,
    CAST(EXTRACT(DAY from payday) AS integer) AS day
FROM loan
;
