#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#


# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return strs
        for i in range(len(strs[0])):
            letter = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != letter:
                    return strs[0][:i]
        return strs[0]


# @lc code=end
