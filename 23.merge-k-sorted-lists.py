#
# @lc app=leetcode id=23 lang=python
#
# [23] Merge k Sorted Lists
#


# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        temp = []
        for i in lists:
            node = i
            while node is not None:
                temp.append(node.val)
                node = node.next

        temp.sort()

        start = ListNode()
        current = start

        for i, v in enumerate(temp):
            current.next = ListNode(v)
            current = current.next

        return start.next


# @lc code=end
