#
# @lc app=leetcode id=38 lang=python
#
# [38] Count and Say
#


# @lc code=start
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        s = "11"
        for _ in range(0, n - 2):
            s = self.recursion(s)
        return s

    def recursion(self, s):
        """
        :type s: str
        :rtype: str
        """
        previous = ""
        result = ""
        count = 0
        for i in range(len(s)):
            if i == 0:  # 第一個
                previous = s[i]
                count = 1
            elif i == len(s) - 1:  # 最後一個
                if s[i] == previous:
                    result += str(count + 1) + s[i]
                else:
                    result += str(count) + previous
                    result += "1" + s[i]
            elif s[i] == previous:
                count += 1
            else:
                result += str(count) + previous
                count = 1
                previous = s[i]
        return result


# @lc code=end
