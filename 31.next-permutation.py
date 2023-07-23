#
# @lc app=leetcode id=31 lang=python
#
# [31] Next Permutation
#


# @lc code=start
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        targetlist = []
        for i in nums:
            targetlist.append(i)

        targetlist.sort(reverse=True)
        if nums == targetlist:
            nums.sort()
            return

        targetIndex = 0
        # 找到右邊大於左邊的位置
        for i in reversed(range(len(nums))):
            if nums[i - 1] < nums[i]:
                targetIndex = i - 1
                break
        # 找到剛好大於目標位置的位置
        for i in reversed(range(targetIndex, len(nums))):
            if nums[i] > nums[targetIndex]:
                nums[i], nums[targetIndex] = nums[targetIndex], nums[i]
                break

        targetIndex += 1
        targetlist = nums[targetIndex:]
        targetlist.sort()
        for i in range(0, len(targetlist)):
            firstindex = nums.index(targetlist[i], targetIndex)
            nums[firstindex], nums[targetIndex] = nums[targetIndex], nums[firstindex]
            targetIndex += 1


# @lc code=end
