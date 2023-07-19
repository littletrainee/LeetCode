#
# @lc app=leetcode id=7 lang=python
#
# [7] Reverse Integer
#

# @lc code=start
import sys


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        isnegative = False

        if x < 0:
            isnegative = True
            x *= -1

        while x > 0:
            if result * 10 > 2**31 - 1:
                return 0
            result = result * 10 + x % 10
            x //= 10

        if isnegative:
            result *= -1

        return result


# @lc code=end
