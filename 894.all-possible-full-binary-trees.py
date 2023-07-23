#
# @lc app=leetcode id=894 lang=python
#
# [894] All Possible Full Binary Trees
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n % 2 == 0 or n < 1:
            return []

        return self.generate_FBT(n)

    def generate_FBT(self, remain):
        """
        :type remain:int
        :rtype: List[TreeNode]
        """
        if remain == 1:
            return [TreeNode(0)]

        res = []
        for i in range(1, remain, 2):
            left_subtrees = self.generate_FBT(i)
            right_subtrees = self.generate_FBT(remain - 1 - i)

            for left_subtree in left_subtrees:
                for right_subtree in right_subtrees:
                    root = TreeNode(0)
                    root.left = left_subtree
                    root.right = right_subtree
                    res.append(root)

        return res


# def inorder_traversal(root):
#     if not root:
#         return
#     if type(root.left) != TreeNode:
#         print(root.left, end=", ")
#     else:
#         inorder_traversal(root.left)

#     print(root.val, end=", ")

#     if type(root.right) != TreeNode:
#         print(root.right, end=", ")
#     else:
#         inorder_traversal(root.right)


# n = 7
# s = Solution()
# t = s.allPossibleFBT(n)
# for i in t:
#     inorder_traversal(i)


# @lc code=end
