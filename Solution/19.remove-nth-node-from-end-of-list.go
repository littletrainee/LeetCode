package LeetCode

/*
 * @lc app=leetcode id=19 lang=golang
 *
 * [19] Remove Nth Node From End of List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	var (
		currentNode *ListNode = head
		findEndNode *ListNode = head
	)

	// Move the findEndNode pointer n nodes ahead
	for i := 0; i < n; i++ {
		findEndNode = findEndNode.Next
	}

	// If findEndNode is nil, it means the head node needs to be removed
	if findEndNode == nil {
		return head.Next
	}

	// Move both pointers until second reaches the end
	for findEndNode.Next != nil {
		currentNode = currentNode.Next
		findEndNode = findEndNode.Next
	}

	// Remove the nth node from the end
	currentNode.Next = currentNode.Next.Next

	return head
}

// @lc code=end
