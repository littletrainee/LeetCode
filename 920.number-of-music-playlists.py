#
# @lc app=leetcode id=920 lang=python
#
# [920] Number of Music Playlists
#


# @lc code=start
class Solution(object):
    def numMusicPlaylists(self, n, goal, k):
        """
        :type n: int
        :type goal: int
        :type k: int
        :rtype: int
        """
        if n > goal:
            return 0

        preDP = [0] * (n + 1)
        preDP[0] = 1
        for j in range(1, goal + 1):
            curDP = [0] * (n + 1)
            for i in range(j + 1):
                if i > n:
                    break
                if i > k:
                    curDP[i] += preDP[i] * (i - k)
                if i > 0 and i - 1 < n:
                    curDP[i] += preDP[i - 1] * (n - (i - 1))
            preDP = curDP
        return preDP[n] % (10**9 + 7)


# @lc code=end
