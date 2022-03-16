# Write your MySQL query statement below
SELECT name as Employee
FROM(
    SELECT e.id,
    name,
    salary,
    managerID,
    managerS
    from 
    Employee e
    LEFT JOIN(
        select distinct id, salary as managerS
        from Employee
    ) m
    on e.managerID = m.id
)al
where salary > managerS
