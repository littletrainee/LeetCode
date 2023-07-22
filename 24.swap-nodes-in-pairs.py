#
# @lc app=leetcode id=24 lang=python
#
# [24] Swap Nodes in Pairs
#


# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        length = 0
        current = head
        while True:
            length += 1
            if not current.next:
                break
            else:
                current = current.next

        current = head

        if length % 2 == 1:
            while length != 1:
                nextVal = current.next.val
                current.next.val = current.val
                current.val = nextVal
                current = current.next.next
                length -= 2

        else:
            while length != 0:
                nextVal = current.next.val
                current.next.val = current.val
                current.val = nextVal
                current = current.next.next
                length -= 2

        return head


s = Solution()
s.swapPairs(None)

# @lc code=end
