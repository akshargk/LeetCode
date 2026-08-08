CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    declare val int;
    set val = n-1;
  RETURN (
      # Write your MySQL query statement below.
      select distinct salary 
      from Employee
      order by salary desc
      limit val,1
  );
END