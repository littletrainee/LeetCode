#
# @lc app=leetcode id=29 lang=python
#
# [29] Divide Two Integers
#


# @lc code=start
import math


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return None
        result = float(dividend) / float(divisor)
        if result == 2147483648:
            result -= 1
        isNegative = False
        if result < 0:
            result *= -1
            isNegative = True

        result = math.floor(result)
        if isNegative:
            result *= -1
        return int(result)


# @lc code=end
