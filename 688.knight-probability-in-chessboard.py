#
# @lc app=leetcode id=688 lang=python
#
# [688] Knight Probability in Chessboard
#


# @lc code=start
class Solution(object):
    def knightProbability(self, n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        # dp = [[0 for _ in range(n)] for _ in range(n)]
        dp = []
        for i in range(n):
            dp.append([0] * n)
        dp[row][column] = 1

        knightProbablyMoving = [
            (-2, -1),
            (-1, -2),
            (1, -2),
            (2, -1),
            (2, 1),
            (1, 2),
            (-1, 2),
            (-2, 1),
        ]

        for _ in range(k):
            # 建立可以核對的陣列
            dp_next = []
            for i in range(n):
                dp_next.append([0] * n)
            for i in range(n):
                for j in range(n):
                    for dx, dy in knightProbablyMoving:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < n:
                            dp_next[x][y] += dp[i][j] / 8.0

            dp = dp_next

        result_prob = 0
        for i in range(n):
            for j in range(n):
                result_prob += dp[i][j]
        return result_prob


n = 3
k = 2
row = 0
column = 0
s = Solution()
s.knightProbability(n, k, row, column)

# @lc code=end
