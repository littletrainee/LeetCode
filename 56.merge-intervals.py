#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
#


# @lc code=start
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        i = 0
        while True:
            if intervals[i][1] >= intervals[i + 1][0]:
                if intervals[i][1] < intervals[i + 1][1]:
                    intervals[i][1], intervals[i + 1][1] = (
                        intervals[i + 1][1],
                        intervals[i][1],
                    )
                intervals.pop(i + 1)

            else:
                i += 1

            if i == len(intervals) - 1:
                break
        return intervals


# @lc code=end
