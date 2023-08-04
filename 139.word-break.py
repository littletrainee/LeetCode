#
# @lc app=leetcode id=139 lang=python
#
# [139] Word Break
#


# @lc code=start
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        ok = [True]
        for i in range(1, len(s) + 1):
            current_ok = False
            for j in range(i):
                temp = s[j:i]
                if ok[j] and temp in wordDict:
                    current_ok = True
                    break
            ok.append(current_ok)
        return ok[-1]


# @lc code=end
