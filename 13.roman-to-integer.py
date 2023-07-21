#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#


# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        sum_value = 0
        previous_value = 0
        current_value = 0

        for char in s:
            current_value = roman_to_value[char]

            if current_value > previous_value:
                sum_value -= 2 * previous_value

            sum_value += current_value
            previous_value = current_value

        return sum_value


# @lc code=end
