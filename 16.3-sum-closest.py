#
# @lc app=leetcode id=16 lang=python
#
# [16] 3Sum Closest
#


# @lc code=start
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums) - 1
        closestSum = nums[0] + nums[1] + nums[2]
        closestDiff = abs(target - closestSum)
        sum_val = 0
        difference = 0

        for start in range(length - 1):
            left, right = start + 1, length
            while left < right:
                sum_val = nums[start] + nums[left] + nums[right]
                difference = abs(target - sum_val)

                if difference < closestDiff:
                    closestDiff = difference
                    closestSum = sum_val

                if sum_val < target:
                    left += 1
                elif sum_val > target:
                    right -= 1
                else:
                    return sum_val

        return closestSum


# @lc code=end
