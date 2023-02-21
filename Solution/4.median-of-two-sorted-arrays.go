package LeetCode

import "sort"

/*
 * @lc app=leetcode id=4 lang=golang
 *
 * [4] Median of Two Sorted Arrays
 */

// @lc code=start
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	var (
		// Combine both arrays into one array
		num []int = append(nums1, nums2...)
		// Find the middle index of the combined array
		m int = len(num) / 2
	)

	// Sort the combined array in ascending order
	sort.Ints(num)

	// Check if the combined array has odd or even number of elements
	if len(num)%2 == 1 {
		// If the combined array has odd number of elements, return the middle
		// element
		return float64(num[m])
	}

	// If the combined array has even number of elements, return the average of
	// the two middle elements
	return float64(num[m-1]+num[m]) / 2
}

// @lc code=end
