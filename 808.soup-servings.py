#
# @lc app=leetcode id=808 lang=python
#
# [808] Soup Servings
#


# @lc code=start
class Solution(object):
    def soupServings(self, n):
        """
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 0.5
        if n > 4275:
            return 1
        n = n // 25 + (n % 25 > 0)
        dp = {}
        return self.dfs(n, n, dp)

    def dfs(self, a, b, dp):
        if (a, b) in dp:
            return dp[(a, b)]
        if a <= 0 and b <= 0:
            return 0.5
        if a <= 0:
            return 1
        if b <= 0:
            return 0

        dp[(a, b)] = 0.25 * (
            self.dfs(a - 4, b, dp)
            + self.dfs(a - 3, b - 1, dp)
            + self.dfs(a - 2, b - 2, dp)
            + self.dfs(a - 1, b - 3, dp)
        )
        return dp[(a, b)]


# @lc code=end
