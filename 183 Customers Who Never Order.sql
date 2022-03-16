# Write your MySQL query statement below
SELECT name as 'Customers'
FROM(
    SELECT al1.id,
    name,
    IFNULL(orders,0) as orders
    FROM(
        SELECT id,
        name,
        orders
        FROM Customers c
        LEFT JOIN(
            SELECT customerId,
            COUNT(customerId) OVER(PARTITION BY customerId) as orders
            FROM Orders
        )o
        on c.id = o.customerId
    )al1
)al2
where orders = 0
