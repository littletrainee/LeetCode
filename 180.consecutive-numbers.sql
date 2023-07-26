--
-- @lc app=leetcode id=180 lang=mysql
--
-- [180] Consecutive Numbers
--
-- @lc code=start
# Write your MySQL query statement below
WITH cte AS (
    SELECT num,
        lead(num, 1) over() num1,
        lead(num, 2) over() num2
    FROM LOGS
)
SELECT DISTINCT num ConsecutiveNums
FROM cte
WHERE (num = num1)
    AND (num = num2);

-- @lc code=end