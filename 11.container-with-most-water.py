#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#


# @lc code=start
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1:
            return 0

        max_area = 0

        left, right = 0, len(height) - 1
        while left < right:
            if height[left] < height[right]:
                max_area = max(max_area, height[left] * (right - left))
                left += 1
            else:
                max_area = max(max_area, height[right] * (right - left))
                right -= 1

        return max_area


# @lc code=end
