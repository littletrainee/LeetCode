--
-- @lc app=leetcode id=175 lang=mysql
--
-- [175] Combine Two Tables
--
-- @lc code=start
# Write your MySQL query statement below
SELECT p.firstname,
    p.lastname,
    a.city,
    a.state
FROM person AS p
    LEFT JOIN `address` AS a ON p.personid = a.personid;

-- @lc code=end