#
# @lc app=leetcode id=61 lang=python
#
# [61] Rotate List
#


# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None

        lastElement = head
        length = 1
        while lastElement.next:
            lastElement = lastElement.next
            length += 1

        k = k % length

        lastElement.next = head

        tempNode = head
        for _ in range(length - k - 1):
            tempNode = tempNode.next

        answer = tempNode.next
        tempNode.next = None

        return answer


# @lc code=end
