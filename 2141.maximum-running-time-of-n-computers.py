#
# @lc app=leetcode id=2141 lang=python
#
# [2141] Maximum Running Time of N Computers
#


# @lc code=start
class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        batteries.sort()
        total = 0
        for i in batteries:
            total += i
        while batteries[-1] > total // n:
            n -= 1
            total -= batteries.pop()
        return total // n


# @lc code=end
