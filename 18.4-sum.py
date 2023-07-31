#
# @lc app=leetcode id=18 lang=python
#
# [18] 4Sum
#


# @lc code=start
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        lastindex = len(nums) - 1

        for first in range(lastindex - 2):
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            for second in range(first + 1, lastindex - 1):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue

                left = second + 1
                right = lastindex

                while left < right:
                    sum = nums[first] + nums[second] + nums[left] + nums[right]

                    if sum < target:
                        left += 1
                    elif sum > target:
                        right -= 1
                    else:
                        results.append(
                            [nums[first], nums[second], nums[left], nums[right]]
                        )

                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

        return results


# @lc code=end
