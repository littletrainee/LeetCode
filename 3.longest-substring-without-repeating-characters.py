#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.asciiArr = [0] * 128
        self.left = 0
        self.right = 0
        self.maxLen = 0

        while self.right < len(s):
            c = ord(s[self.right])
            self.right += 1
            self.asciiArr[c] += 1

            while self.asciiArr[c] > 1:
                d = ord(s[self.left])
                self.left += 1
                self.asciiArr[d] -= 1

            if self.right - self.left > self.maxLen:
                self.maxLen = self.right - self.left

        return self.maxLen


# @lc code=end
