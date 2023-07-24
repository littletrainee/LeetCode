#
# @lc app=leetcode id=34 lang=python
#
# [34] Find First and Last Position of Element in Sorted Array
#


# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = -1
        second = -1
        for i in range(len(nums)):
            if nums[i] == target:
                first = i
                break

        for i in reversed(range(len(nums))):
            if nums[i] == target:
                second = i
                break
        return [first, second]


# @lc code=end
