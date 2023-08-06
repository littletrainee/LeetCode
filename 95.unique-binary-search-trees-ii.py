#
# @lc app=leetcode id=95 lang=python
#
# [95] Unique Binary Search Trees II
#


# @lc code=start
# Definition for a binary tree node.
import math


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.generate(1, n)

    def generate(self, first, last):
        trees = []
        for root in range(first, last + 1):
            for left in self.generate(first, root - 1):
                for right in self.generate(root + 1, last):
                    node = TreeNode(root)
                    node.left = left
                    node.right = right
                    trees += (node,)
        return trees or [None]


n = 3
s = Solution()
s.generateTrees(n)


# @lc code=end
