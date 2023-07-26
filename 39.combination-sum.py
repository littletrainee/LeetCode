#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#


# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = []
        for _ in range(target + 1):
            dp.append([])
        for c in candidates:
            for i in range(c, target + 1):
                if i == c:
                    dp[i].append([c])
                for comb in dp[i - c]:
                    dp[i].append(comb + [c])
        return dp[-1]


candidates = [2, 3, 5]
target = 8

s = Solution()
print(s.combinationSum(candidates, target))

# @lc code=end
