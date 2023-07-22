#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#


# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        rt = 0
        for i in range(len(nums)):
            if nums[rt] != nums[i]:
                rt += 1
                nums[rt] = nums[i]
        return rt + 1


# @lc code=end
