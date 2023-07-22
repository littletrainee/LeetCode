#
# @lc app=leetcode id=25 lang=python
#
# [25] Reverse Nodes in k-Group
#


# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        current = head
        length = 0
        temp = []
        while current != None:
            length += 1
            temp.append(current.val)
            current = current.next

        clone = []
        # 拆分list到反轉並添加到clone
        for i in range(0, length, k):
            t = temp[i : i + k]
            if len(t) == k:
                t.reverse()
            clone += t

        head = ListNode()
        current = head
        for i, v in enumerate(clone):
            current.next = ListNode(v)
            current = current.next

        return head.next


# @lc code=end
