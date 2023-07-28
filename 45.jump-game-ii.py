#
# @lc app=leetcode id=45 lang=python
#
# [45] Jump Game II
#


# @lc code=start
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums) - 1
        start = 0
        end = 0
        step = 0
        while end < length:
            step += 1
            maxend = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= length:
                    return step
                maxend = max(maxend, i + nums[i])
            start = end + 1
            end = maxend
        return step


# @lc code=end
