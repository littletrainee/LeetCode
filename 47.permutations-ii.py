#
# @lc app=leetcode id=47 lang=python
#
# [47] Permutations II
#


# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        length = len(nums)
        self.backtrack(nums, length, 0, result)
        return result

    def backtrack(self, nums, length, start, result):
        if start == length:
            if nums[:] not in result:
                result.append(nums[:])
            return

        for i in range(start, length):
            nums[start], nums[i] = nums[i], nums[start]
            self.backtrack(nums, length, start + 1, result)
            nums[start], nums[i] = nums[i], nums[start]


# @lc code=end
