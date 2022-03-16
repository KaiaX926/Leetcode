# Write your MySQL query statement below

SELECT DISTINCT email as Email
from(
    SELECT email,
    COUNT(id) OVER(PARTITION BY email) as numbers
    FROM Person
)a
WHERE numbers > 1
