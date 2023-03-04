package LeetCode

import (
	"fmt"
	"testing"
)

func TestSolution(t *testing.T) {
	// head := &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 3, Next: &ListNode{Val: 4, Next: &ListNode{Val: 5, Next: nil}}}}}
	head := &ListNode{Val: 1, Next: &ListNode{Val: 2}}
	n := 2
	head = removeNthFromEnd(head, n)
	for head != nil {
		fmt.Println(head)
		head = head.Next
	}
}
