package main

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
type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	var (
		dummyHead *ListNode = &ListNode{Val: 0}
		carried   int
		current   *ListNode = dummyHead
		l1Val     int
		l2Val     int
	)
	for l1 != nil || l2 != nil || carried != 0 {
		if l1 != nil {
			l1Val = l1.Val
			l1 = l1.Next
		} else {
			l1Val = 0
		}
		if l2 != nil {
			l2Val = l2.Val
			l2 = l2.Next
		} else {
			l2Val = 0
		}
		columSum := l1Val + l2Val + carried
		carried = columSum / 10
		current.Next = &ListNode{Val: columSum % 10}
		current = current.Next
	}
	return dummyHead.Next
}

// @lc code=end
