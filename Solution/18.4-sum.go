package LeetCode

import "sort"

/*
 * @lc app=leetcode id=18 lang=golang
 *
 * [18] 4Sum
 */

// @lc code=start
func fourSum(nums []int, target int) [][]int {
	sort.Ints(nums) // Sort the array in ascending order
	var (
		// Initialize a two-dimensional slice to store the results
		results [][]int
		// Get the index of the last element in the array
		lastindex = len(nums) - 1
		sum       int
	)

	// Loop through the array from the beginning
	for first := 0; first < lastindex-2; first++ {
		// Skip the current iteration if the current element is the same as the
		// previous element and not the first element
		if first > 0 && nums[first] == nums[first-1] {
			continue
		}
		// Loop through the array from the next element after start
		for second := first + 1; second < lastindex-1; second++ {
			// Skip the current iteration if the current element is the same as
			// the previous element and not the first element after start
			if second > first+1 && nums[second] == nums[second-1] {
				continue
			}

			// Use two pointers, left and right, to traverse the remaining
			// elements in the array
			for left, right := second+1, lastindex; left < right; {
				// Calculate the sum of the four elements
				sum = nums[first] + nums[second] + nums[left] + nums[right]
				// If the sum is less than target, move the left pointer to the
				// right to increase the sum
				if sum < target {
					left++
					continue
				}
				// If the sum is greater than target, move the right pointer to
				// the left to decrease the sum
				if sum > target {
					right--
					continue
				}

				// If the sum equals target, add the four elements to the result
				// and move the left and right pointers to find the next set of
				// four elements that equal target
				results = append(results, []int{nums[first], nums[second],
					nums[left], nums[right]})
				left++
				right--

				// Skip any duplicates of the left and right pointers
				for left < right && nums[left] == nums[left-1] {
					left++
				}
				for left < right && nums[right] == nums[right+1] {
					right--
				}
			}
		}
	}
	// Return the result
	return results
}

// @lc code=end
