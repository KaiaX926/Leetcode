CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT max(salary)
      FROM(
            SELECT id,salary,
            DENSE_RANK() OVER (ORDER BY salary DESC) my_rank
            FROM Employee
      )a
      WHERE my_rank = N
  );
END
