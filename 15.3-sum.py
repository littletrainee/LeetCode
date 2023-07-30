#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#


# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        length = len(nums) - 1
        target = 0
        sum_val = 0

        for start in range(length - 1):
            if start > 0 and nums[start] == nums[start - 1]:
                continue
            target = -nums[start]
            left, right = start + 1, length
            while left < right:
                sum_val = nums[left] + nums[right]
                if sum_val < target:
                    left += 1
                    continue
                if sum_val > target:
                    right -= 1
                    continue
                result.append([nums[start], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

        return result


# @lc code=end
