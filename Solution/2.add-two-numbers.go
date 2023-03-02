package LeetCode

/*
 * @lc app=leetcode id=2 lang=golang
 *
 * [2] Add Two Numbers
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
// type ListNode struct {
// 	Val  int
// 	Next *ListNode
// }

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	// dummyHead is a pointer to a new ListNode object that is used to start the
	// linked list that will store the sum of the two input lists.
	var (
		dummyHead *ListNode = &ListNode{Val: 0}
		current   *ListNode = dummyHead
		carried   uint8
		l1Val     uint8
		l2Val     uint8
		columSum  uint8
	)
	// This loop continues until there are no morenodes left in the input lists,
	// and there is no carried value remaining.
	for l1 != nil || l2 != nil || carried != 0 {
		// l1Val and l2Val are the values of the current nodes in the input
		// lists. If one of the lists has already reached the end, then l1Val or
		// l2Val is set to 0.
		if l1 != nil {
			l1Val = uint8(l1.Val)
			l1 = l1.Next
		} else {
			l1Val = 0
		}
		if l2 != nil {
			l2Val = uint8(l2.Val)
			l2 = l2.Next
		} else {
			l2Val = 0
		}
		// columSum is the sum of the current column, which is the sum of l1Val,
		// l2Val, and any carried value from the previous column.
		columSum = l1Val + l2Val + carried
		// carried is set to the integer division of columSum by 10. This is
		// because if the sum of two digits is greater than or equal to 10, then
		// there is a carried value that must be added to the next column.
		carried = columSum / 10
		// A new ListNode object is created with the value equal to the
		// remainder of columSum divided by 10. This is the value that is stored
		// in the current column.
		current.Next = &ListNode{Val: int(columSum % 10)}
		// The current pointer is moved to the next node in the list.
		current = current.Next
	}
	// The dummyHead pointer points to the first node in the linked list that
	// was created. Since the first node is a dummy node, the actual first node
	// is the node after the dummy node.
	return dummyHead.Next
}

// @lc code=end
