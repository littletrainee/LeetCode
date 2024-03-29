#
# @lc app=leetcode id=33 lang=python
#
# [33] Search in Rotated Sorted Array
#


# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1


# @lc code=end
