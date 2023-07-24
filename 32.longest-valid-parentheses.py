#
# @lc app=leetcode id=32 lang=python
#
# [32] Longest Valid Parentheses
#


# @lc code=start
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 用來記錄括號的位置，初始化為-1，當作假想的右括號前一個位置
        stack = [-1]
        max_length = 0

        for i in range(len(s)):
            if s[i] == "(":
                # 將左括號的位置加入堆疊
                stack.append(i)
            else:
                # 遇到右括號，移除堆疊中的左括號位置
                stack.pop()
                if not stack:
                    # 如果堆疊為空，將右括號位置加入堆疊當作假想的右括號前一個位置
                    stack.append(i)
                else:
                    # 計算有效括號的長度
                    max_length = max(max_length, i - stack[-1])

        return max_length


# @lc code=end
