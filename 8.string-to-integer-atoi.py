#
# @lc app=leetcode id=8 lang=python
#
# [8] String to Integer (atoi)
#

# @lc code=start
import math


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        isnegative = False
        started = False

        for v in s:
            if v.isdigit():
                started = True
                digit = int(v)
                result = result * 10 + digit
                if not isnegative and result > math.pow(2, 31) - 1:
                    return int(math.pow(2, 31) - 1)
                if isnegative and -result < -math.pow(2, 31):
                    return int(-math.pow(2, 31))
            elif v == "+" and not started:
                started = True
            elif v == "-" and not started:
                started = True
                isnegative = True
            elif v != " " or started:
                break

        if isnegative:
            result *= -1

        return result


# @lc code=end
