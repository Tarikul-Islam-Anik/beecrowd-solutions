SELECT
	'Podium: ' || team AS name
FROM league
WHERE position <= 3
UNION ALL
SELECT
	'Demoted: ' || team AS name
FROM league
WHERE position IN (SELECT position
				   FROM league
				   ORDER BY position DESC
				   LIMIT 2)
: