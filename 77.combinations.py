#
# @lc app=leetcode id=77 lang=python
#
# [77] Combinations
#


# @lc code=start
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []

        self.backtrack(1, [], n, k, result)
        return result

    def backtrack(self, start, temp, n, k, result):
        if len(temp) == k and sorted(temp) not in result:
            result.append(temp[:])
            return

        for i in range(start, n + 1):
            temp.append(i)
            self.backtrack(i + 1, temp, n, k, result)
            temp.pop()


# @lc code=end
