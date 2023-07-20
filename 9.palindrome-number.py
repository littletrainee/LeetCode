#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#


# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True

        reverse = 0
        temp = x

        while temp is not 0:
            remainder = temp % 10
            temp /= 10
            reverse = reverse * 10 + remainder

        return reverse == x


# @lc code=end
