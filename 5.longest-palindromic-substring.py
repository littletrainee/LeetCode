#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#


# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 1:
            return ""

        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            if len1 > len2 and len1 > end - start:
                start = i - len1 / 2
                end = i + len1 / 2
                continue
            if len2 > end - start:
                start = i - len2 / 2 + 1
                end = i + len2 / 2
                continue

        return s[start : end + 1]

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1


# @lc code=end
