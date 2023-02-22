package LeetCode

import (
	"fmt"
	"testing"
)

func TestSolution(t *testing.T) {
	var (
		s string = "aab"
		p string = "c*a*b"
	)
	fmt.Println(isMatch(s, p))
}
