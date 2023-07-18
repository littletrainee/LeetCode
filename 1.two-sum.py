#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#


# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.indexmap = {}

        for i, v in enumerate(nums):
            if target - v in self.indexmap:
                return [self.indexmap[target - v], i]
            self.indexmap[v] = i

        return []


# @lc code=end
