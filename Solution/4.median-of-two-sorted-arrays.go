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
		// merge two slice
		num []int = append(nums1, nums2...)
		// get the center index
		m int = len(num) / 2
	)
	sort.Ints(num)
	// len(num) = 奇數
	if len(num)%2 == 1 {
		return float64(num[m])
	}
	// len(num) = 偶數
	return float64(num[m-1]+num[m]) / 2
}

// @lc code=end
