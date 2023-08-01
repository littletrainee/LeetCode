#
# @lc app=leetcode id=57 lang=python
#
# [57] Insert Interval
#


# @lc code=start
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
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
