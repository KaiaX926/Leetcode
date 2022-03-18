WITH r_t as(
    SELECT *,
    ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) as r_m
    FROM person
    )

DELETE FROM person
WHERE id IN (
    SELECT id
    FROM r_t
    WHERE r_m > 1
    )

