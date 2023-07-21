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
        longest_lengths = [1] * length
        counts = [1] * length

        for i in range(length):
            for j in range(i):
                if nums[j] < nums[i]:
                    if longest_lengths[i] < longest_lengths[j] + 1:
                        longest_lengths[i] = longest_lengths[j] + 1
                        counts[i] = counts[j]
                    elif longest_lengths[i] == longest_lengths[j] + 1:
                        counts[i] += counts[j]

        max_length = max(longest_lengths)

        result_count = 0
        for length, count in zip(longest_lengths, counts):
            if length == max_length:
                result_count += count

        return result_count


# @lc code=end
