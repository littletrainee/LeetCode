#
# @lc app=leetcode id=62 lang=python
#
# [62] Unique Paths
#


# @lc code=start
import math


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not m or not n:
            return 0
        return math.factorial(m + n - 2) / (
            math.factorial(n - 1) * math.factorial(m - 1)
        )

    # O(m*n) space
    def uniquePaths2(self, m, n):
        if not m or not n:
            return 0
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    # O(n) space
    def uniquePaths(self, m, n):
        if not m or not n:
            return 0
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j - 1]
        return cur[-1]


# @lc code=end
