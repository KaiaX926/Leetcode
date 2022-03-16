# Write your MySQL query statement below
select 
firstName, 
lastName, 
city, 
state
from 
Person P
Left join 
Address A
on P.personId = A.personId
