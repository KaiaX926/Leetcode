# Write your MySQL query statement below
SELECT Department,
name as Employee,
salary
FROM(
    SELECT e.id,
    e.name,
    salary,
    d.name as Department,
    RANK() OVER(PARTITION BY d.name ORDER BY salary DESC) as rank_number
    FROM Employee e
    LEFT JOIN Department d
    on d.id = e.departmentId
)all1
where rank_number = 1
