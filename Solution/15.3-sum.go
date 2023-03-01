package LeetCode

import "sort"

/*
 * @lc app=leetcode id=15 lang=golang
 *
 * [15] 3Sum
 */

// @lc code=start
func threeSum(nums []int) [][]int {
	// sort the input array in ascending order
	sort.Ints(nums)
	var result [][]int
	var length int = len(nums) - 1
	var target int
	var sum int
	for start := 0; start < length-1; start++ {
		// skip duplicate elements to avoid duplicates in the result
		if start > 0 && nums[start] == nums[start-1] {
			continue
		}
		// set the target value as the negative of the current element
		target = -nums[start]
		// use two pointers to find two elements that sum up to the target value
		for left, right := start+1, length; left < right; {
			sum = nums[left] + nums[right]
			if sum < target {
				// move the left pointer to the right to increase the sum
				left++
				continue
			}
			if sum > target {
				// move the right pointer to the left to decrease the sum
				right--
				continue
			}
			// found a triplet that sums up to zero, add it to the result
			result = append(result, []int{nums[start], nums[left], nums[right]})
			// skip duplicate elements to avoid duplicates in the result
			for left < right && nums[left] == nums[left+1] {
				left++
			}
			for left < right && nums[right] == nums[right-1] {
				right--
			}
			// move both pointers to find other potential triplets
			left++
			right--
		}
	}
	return result
}

// @lc code=end
