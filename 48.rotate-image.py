#
# @lc app=leetcode id=48 lang=python
#
# [48] Rotate Image
#


# @lc code=start
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        if length <= 1:
            return matrix
        result = {}
        for i in range(length):
            temp = []
            for j in range(length - 1, -1, -1):
                temp.append(matrix[j][i])
            result[i] = temp

        for i in range(length):
            matrix[i] = result[i]


# @lc code=end
