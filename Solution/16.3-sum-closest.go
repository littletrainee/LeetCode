package LeetCode

import (
	"sort"
)

/*
 * @lc app=leetcode id=16 lang=golang
 *
 * [16] 3Sum Closest
 */

// @lc code=start
func threeSumClosest(nums []int, target int) int {
	// Sort the array of numbers.
	sort.Ints(nums)

	// Initialize variables to keep track of the closest sum and its difference
	// to the target.
	var (
		length      int = len(nums) - 1
		closestSum  int = nums[0] + nums[1] + nums[2]
		closestDiff int = abs(target - closestSum)
		sum         int
		difference  int
	)

	// Loop through each element in the sorted array as a possible starting
	// point.
	for start := 0; start < length-1; start++ {
		// Use two pointers to find the closest sum to the target.
		for left, right := start+1, length; left < right; {
			// Calculate the current sum and its difference to the target.
			sum = nums[start] + nums[left] + nums[right]
			difference = abs(target - sum)

			// If the current difference is smaller than the previous closest
			// difference, update the closest sum and difference.
			if difference < closestDiff {
				closestDiff = difference
				closestSum = sum
			}

			// Move the left or right pointer depending on whether the current
			// sum is smaller or larger than the target.
			if sum < target {
				left++
			} else if sum > target {
				right--
			} else {
				// If the current sum is equal to the target, return the sum.
				return sum
			}
		}
	}

	// If no sum is equal to the target, return the closest sum.
	return closestSum
}

// A function to calculate the absolute value of an integer.
func abs(x int) int {
	mask := x >> 31
	return (x + mask) ^ mask
}

// @lc code=end
