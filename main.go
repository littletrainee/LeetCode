package main

import (
	"LeetCode/Solution"
	"fmt"
)

func main() {
	var (
		nums   []int = []int{2, 7, 11, 15}
		target int   = 9
	)
	fmt.Println(Solution.TwoSum(nums, target))
}
