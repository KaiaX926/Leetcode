# Write your MySQL query statement below
with t1 as(
    select 
    num,
    num-lead(num,1) over(order by id) as first,
    num-lead(num,2) over(order by id) as second 
    from Logs
)

select distinct num as ConsecutiveNums
from t1
where first = 0 and second = 0


#For example, by using the LEAD() function, from the current row, you can access data of the next row, or the row after the next row, and so on.
