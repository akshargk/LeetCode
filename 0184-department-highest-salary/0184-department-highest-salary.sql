# Write your MySQL query statement below
select d.name as Department,e.name as Employee, e.salary from employee e
left join department d on d.id = e.departmentid
where e.salary = (select max(e1.salary) from employee e1 where e.departmentid = e1.departmentid) 