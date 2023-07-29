#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#


# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.backtrack(nums, 0, result)
        return result

    def backtrack(self, nums, start, result):
        if start == len(nums):
            result.append(nums[:])
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]  # 交换元素
            self.backtrack(nums, start + 1, result)  # 递归求解剩余元素的全排列
            nums[start], nums[i] = nums[i], nums[start]  # 回溯，恢复原始顺序


# @lc code=end
