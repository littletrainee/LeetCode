package LeetCode

/*
 * @lc app=leetcode id=11 lang=golang
 *
 * [11] Container With Most Water
 */

// @lc code=start
func maxArea(height []int) int {
	if len(height) <= 1 {
		return 0
	}

	// Initialize variables for storing max area and the two pointers
	var max int
	// var max float64

	// Iterate through the array while the two pointers don't overlap
	for left, right := 0, len(height)-1; left <= right; {
		// Calculate the area between the two pointers and update max if necessary
		if height[left] < height[right] {
			max = Max(max, height[left]*(right-left))
			// max = math.Max(max, float64(height[left]*(right-left)))
			left++
		} else {
			max = Max(max, height[right]*(right-left))
			// max = math.Max(max, float64(height[right]*(right-left)))
			right--
		}
	}

	// Return the maximum area
	return max
}

func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

// @lc code=end
