#
# @lc app=leetcode id=852 lang=python
#
# [852] Peak Index in a Mountain Array
#


# @lc code=start
class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        return arr.index(max(arr))


# @lc code=end
