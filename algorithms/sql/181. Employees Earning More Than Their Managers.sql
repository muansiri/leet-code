# Write your MySQL query statement below
SELECT E.name AS Employee from Employee AS E INNER JOIN Employee AS M ON E.managerId = M.id WHERE E.salary > M.salary;