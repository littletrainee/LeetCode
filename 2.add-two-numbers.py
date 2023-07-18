#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#


# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        self.dummyHead = ListNode(0)
        self.current = self.dummyHead
        self.carried = 0

        while l1 or l2 or self.carried:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            column_sum = l1_val + l2_val + self.carried
            self.carried = column_sum // 10

            self.current.next = ListNode(column_sum % 10)
            self.current = self.current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return self.dummyHead.next


# @lc code=end
