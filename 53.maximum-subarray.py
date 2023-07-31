#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#


# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Max = nums[0]
        currentsum = nums[0]

        for i in range(1, len(nums)):
            currentsum = max(nums[i], currentsum + nums[i])
            Max = max(Max, currentsum)

        return Max


# @lc code=end
