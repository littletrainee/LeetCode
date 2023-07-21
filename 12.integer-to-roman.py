#
# @lc app=leetcode id=12 lang=python
#
# [12] Integer to Roman
#


# @lc code=start
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        RomanNumerals = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

        placeValue = 1
        romanStr = ""

        while num > 0:
            digit = num % 10 * placeValue

            if digit == 9 * placeValue:
                romanStr = RomanNumerals[9 * placeValue] + romanStr
            elif digit >= 5 * placeValue:
                t = RomanNumerals[5 * placeValue]
                digit -= 5 * placeValue
                for j in range(digit // placeValue):
                    t += RomanNumerals[1 * placeValue]
                romanStr = t + romanStr
            elif digit == 4 * placeValue:
                romanStr = RomanNumerals[4 * placeValue] + romanStr
            else:
                t = ""
                for j in range(digit // placeValue):
                    t += RomanNumerals[1 * placeValue]
                romanStr = t + romanStr

            placeValue *= 10
            num //= 10

        return romanStr


# @lc code=end
