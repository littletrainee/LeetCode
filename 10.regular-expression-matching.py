#
# @lc app=leetcode id=10 lang=python
#
# [10] Regular Expression Matching
#


# @lc code=start
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
            return len(s) == 0

        if p[-1] == "*":
            if self.isMatch(s, p[:-2]):
                return True

            return (
                len(s) > 0
                and (p[-2] == "." or s[-1] == p[-2])
                and self.isMatch(s[:-1], p)
            )

        if len(s) > 0 and (p[-1] == "." or s[-1] == p[-1]):
            return self.isMatch(s[:-1], p[:-1])


# @lc code=end
