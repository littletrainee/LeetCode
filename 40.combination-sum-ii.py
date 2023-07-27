#
# @lc app=leetcode id=40 lang=python
#
# [40] Combination Sum II
#


# @lc code=start
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates = sorted(candidates)
        self.dfs(candidates, target, [], res)

        return res

    def dfs(self, candidates, target, path, res):
        if target == 0:
            res.append(path)
            return
        for i in range(len(candidates)):
            if candidates[i] > target or i >= 1 and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(
                candidates[i + 1 :], target - candidates[i], path + [candidates[i]], res
            )


# @lc code=end
