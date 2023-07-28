#
# @lc app=leetcode id=44 lang=python
#
# [44] Wildcard Matching
#


# @lc code=start
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_idx = 0
        p_idx = 0
        s_match = 0
        p_star = -1

        while s_idx < len(s):
            if p_idx < len(p) and (p[p_idx] == "?" or p[p_idx] == s[s_idx]):
                s_idx += 1
                p_idx += 1
            elif p_idx < len(p) and p[p_idx] == "*":
                p_star = p_idx
                s_match = s_idx
                p_idx += 1
            elif p_star != -1:
                p_idx = p_star + 1
                s_match += 1
                s_idx = s_match
            else:
                return False

        while p_idx < len(p) and p[p_idx] == "*":
            p_idx += 1

        return p_idx == len(p)


# @lc code=end
