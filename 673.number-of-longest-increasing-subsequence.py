#
# @lc app=leetcode id=673 lang=python
#
# [673] Number of Longest Increasing Subsequence
#


# @lc code=start
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        length = len(nums)
        lis = [1] * length  # 對應nums順序的當前數字有可以有多少的長度
        counts = [1] * length  # 指的是當前順序子序列的數量

        for index in range(length):
            for beforeIndex in range(index):
                if nums[beforeIndex] < nums[index]:
                    if lis[index] < lis[beforeIndex] + 1:
                        lis[index] = lis[beforeIndex] + 1
                        counts[index] = counts[beforeIndex]
                    elif lis[index] == lis[beforeIndex] + 1:
                        counts[index] += counts[beforeIndex]

        max_length = max(lis)

        result_count = 0
        for length, count in zip(lis, counts):
            if length == max_length:
                result_count += count

        return result_count


x = [1, 3, 5, 4, 7]
s = Solution()
s.findNumberOfLIS(x)

# @lc code=end
