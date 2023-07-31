#
# @lc app=leetcode id=712 lang=python
#
# [712] Minimum ASCII Delete Sum for Two Strings
#


# @lc code=start
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        common = self.lcs(s1, s2)
        total, res = 0, 0
        for c in s1:
            total += ord(c)
        for c in s2:
            total += ord(c)

        res = total - common * 2
        return res

    def lcs(self, s1, s2):
        """
        :type s str
        :type p: str
        :rtype: int
        """
        prev = [0] * (len(s2) + 1)

        for i in range(len(s1)):
            curr = [0] * (len(s2) + 1)
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    curr[j + 1] = prev[j] + ord(s1[i])
                else:
                    curr[j + 1] = max(curr[j], prev[j + 1])
            prev = curr

        return prev[-1]


# @lc code=end
