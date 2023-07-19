#
# @lc app=leetcode id=6 lang=python
#
# [6] Zigzag Conversion
#


# @lc code=start
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2:
            return s

        sliceholder = [[] for _ in range(numRows)]
        reverse = False
        order = 0
        result = []

        for v in s:
            sliceholder[order].append(v)
            if reverse:
                order -= 1
            else:
                order += 1

            if order == numRows - 1:
                reverse = True
            if order == 0:
                reverse = False

        for v in sliceholder:
            result.extend(v)

        return "".join(result)


# @lc code=end
