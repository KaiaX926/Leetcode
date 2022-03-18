# Write your MySQL query statement below
SELECT id
FROM(
    SELECT id,
    recordDate,
    temperature,
    lag(temperature) OVER(ORDER BY recordDate ASC) AS temBefore,
    lag(recordDate) OVER(ORDER BY recordDate ASC) AS DateBefore
    FROM
    Weather
)w
WHERE temperature > temBefore
AND recordDate - DateBefore = 1
