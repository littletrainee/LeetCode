package LeetCode

/*
 * @lc app=leetcode id=21 lang=golang
 *
 * [21] Merge Two Sorted Lists
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	// If one of the lists is empty, return the other list
	if list1 == nil {
		return list2
	}
	if list2 == nil {
		return list1
	}

	var (
		tail      *ListNode = &ListNode{}
		dummyHead *ListNode = tail
	)

	// Traverse both lists and merge them in ascending order
	for list1 != nil || list2 != nil {
		if list1 != nil && (list2 == nil || list1.Val <= list2.Val) {
			// Append the smaller value node to the merged list
			tail.Next = list1
			list1 = list1.Next
		} else {
			tail.Next = list2
			list2 = list2.Next
		}
		// Move the tail pointer to the last node of the merged list
		tail = tail.Next
	}

	// Return the merged list (excluding the dummy head node)
	return dummyHead.Next
}

// @lc code=end
