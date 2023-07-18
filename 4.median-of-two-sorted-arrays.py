#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#


# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        self.num = sorted(nums1 + nums2)

        self.m = len(self.num)

        if self.m % 2 == 0:
            return (float(self.num[self.m / 2 - 1]) + float(self.num[self.m / 2])) / 2

        return self.num[self.m / 2]


# @lc code=end
