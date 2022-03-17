# Write your MySQL query statement below
SELECT Department,
name as Employee,
salary as Salary
FROM(
    SELECT e.*,
    d.name as Department
    FROM (
        SELECT *,
        DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC ) AS rank_number
        FROM Employee
    )e
    LEFT JOIN Department d
    ON e.departmentId = d.id
)all1
where rank_number <= 3
