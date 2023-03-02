package LeetCode

import (
	"fmt"
	"testing"
)

func TestSolution(t *testing.T) {
	var (
		num    []int = []int{4, 0, 5, -5, 3, 3, 0, -4, -5}
		target int   = -2
	)
	fmt.Println(threeSumClosest(num, target))
}
