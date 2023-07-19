#
# @lc app=leetcode id=435 lang=python
#
# [435] Non-overlapping Intervals
#


# @lc code=start
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x: x[1])
        res = 0
        n = len(intervals)
        endLast = intervals[0][1]
        for i in range(1, n):
            if endLast > intervals[i][0]:
                res += 1
            else:
                endLast = intervals[i][1]

        return res


# @lc code=end
