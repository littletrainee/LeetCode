#
# @lc app=leetcode id=55 lang=python
#
# [55] Jump Game
#


# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        destination = len(nums) - 1
        source = destination - 1

        while source >= 0:
            if source + nums[source] >= destination:
                destination = source
            source -= 1
        return destination == 0


# @lc code=end
