#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#


# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.ans = []
        curstr = ""
        self.dfs(curstr, n, 0, 0)
        return self.ans

    def dfs(self, curstr, curselength, left, right):
        if len(curstr) == curselength * 2:
            self.ans.append(curstr)
            return
        else:
            if left < curselength:
                self.dfs(curstr + "(", curselength, left + 1, right)
            if right < left:
                self.dfs(curstr + ")", curselength, left, right + 1)


# @lc code=end
