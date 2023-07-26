#
# @lc app=leetcode id=1870 lang=python
#
# [1870] Minimum Speed to Arrive on Time
#

# @lc code=start
import math


class Solution(object):
    def isPossible(self, dist, speed, hour):
        """
        :type dist: List[int]
        :type speed: int
        :type hour: float
        :rtype: bool
        """
        ans = 0
        for i in range(len(dist)):
            d = dist[i] * 1.0 / speed
            if i != len(dist) - 1:
                ans = ans + math.ceil(d)
            else:
                ans += d
            if ans > hour:
                return False
        return ans <= hour

    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        low = 1
        hight = 10**7
        min_speed = -1
        while low <= hight:
            mid = low + (hight - low) // 2
            if self.isPossible(dist, mid, hour):
                min_speed = mid
                hight = mid - 1
            else:
                low = mid + 1
        return min_speed


dist = [1, 3, 2]
hour = 2.7
s = Solution()
print(s.minSpeedOnTime(dist, hour))

# @lc code=end
