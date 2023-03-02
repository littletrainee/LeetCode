package LeetCode

/*
 * @lc app=leetcode id=1 lang=golang
 *
 * [1] Two Sum
 */

// @lc code=start
func twoSum(nums []int, target int) []int {
	// Create a map to store the index of each element in the nums slice and its
	// corresponding value
	var indexMap map[int]int = make(map[int]int)

	// Loop through the nums slice
	for currentIndex, currentValue := range nums {
		// Calculate the anotherIndex of the current value and target
		if anotherIndex, isExist := indexMap[target-currentValue]; isExist {
			// If the complement is in the indexMap, return the indices of the
			// two elements whose sum equals to the target
			return []int{anotherIndex, currentIndex}
		}
		// Otherwise, add the current value and its index to the indexMap
		indexMap[currentValue] = currentIndex
	}
	// If no two elements sum up to the target, return an empty slice
	return []int{}
}

// @lc code=end
