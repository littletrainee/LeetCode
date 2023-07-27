--
-- @lc app=leetcode id=181 lang=mysql
--
-- [181] Employees Earning More Than Their Managers
--
-- @lc code=start
# Write your MySQL query statement below
SELECT e1.name AS 'Employee'
FROM employee AS e1
    INNER JOIN employee AS e2 ON e1.managerid = e2.id
WHERE e1.salary > e2.salary;

-- @lc code=end