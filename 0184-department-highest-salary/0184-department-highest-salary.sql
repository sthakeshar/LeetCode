# Write your MySQL query statement below
SELECT d.name AS Department, 
       e.name AS Employee, 
       e.salary AS Salary
FROM Employee e
INNER JOIN Department d 
  ON e.departmentid = d.id
WHERE (e.departmentid, e.salary) IN (
    SELECT departmentID, MAX(salary)
    FROM Employee
    GROUP BY departmentID
);
