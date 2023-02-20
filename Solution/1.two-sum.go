package LeetCode

/*
 * @lc app=leetcode id=1 lang=golang
 *
 * [1] Two Sum
 */

// @lc code=start
func twoSum(nums []int, target int) []int {
	// Loop through all pairs of elements in the input array
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			// If the sum of the current pair of elements is equal to the
			// target, return their indices as an array
			if target == nums[i]+nums[j] {
				return []int{i, j}
			}
		}
	}
	// If no pair of elements adds up to the target, return an empty array
	return []int{}
}

// @lc code=end
