#
# @lc app=leetcode id=486 lang=python
#
# [486] Predict the Winner
#


# @lc code=start
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        memo = {}
        return self.canWin(nums, memo, 0, len(nums) - 1) >= 0

    def canWin(self, nums, memo, left, right):
        if left == right:
            return nums[left]

        if (left, right) in memo:
            return memo[(left, right)]

        pickLeft = nums[left] - self.canWin(nums, memo, left + 1, right)
        pickRight = nums[right] - self.canWin(nums, memo, left, right - 1)
        memo[(left, right)] = max(pickLeft, pickRight)
        return memo[(left, right)]


# @lc code=end
