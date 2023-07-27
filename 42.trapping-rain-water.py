#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
#


# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0

        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        result = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    result += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    result += right_max - height[right]
                right -= 1

        return result


# @lc code=end
