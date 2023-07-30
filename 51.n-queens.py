#
# @lc app=leetcode id=51 lang=python
#
# [51] N-Queens
#


# @lc code=start
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        result = []
        stack = [(0, [], [], [])]
        while stack:
            row, queens, xy_dif, xy_sum = stack.pop()

            if row == n:
                result.append(queens)
                continue

            for q in range(n):
                if q not in queens and row - q not in xy_dif and row + q not in xy_sum:
                    new_queens = queens + [q]
                    new_xy_dif = xy_dif + [row - q]
                    new_xy_sum = xy_sum + [row + q]
                    stack.append((row + 1, new_queens, new_xy_dif, new_xy_sum))

        for i in range(len(result)):
            temp = []
            for j in result[i]:
                temp.append("." * j + "Q" + "." * (n - j - 1))
            result[i] = temp
        return result


# @lc code=end
