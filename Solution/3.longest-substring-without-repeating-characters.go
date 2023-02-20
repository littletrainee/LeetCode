package LeetCode

/*
 * @lc app=leetcode id=3 lang=golang
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
func lengthOfLongestSubstring(s string) int {
	// Initialize a map to keep track of the characters and the number of times
	// they appear in the substring
	var (
		dummy               map[byte]uint8 = make(map[byte]uint8)
		left, right, maxLen int
		char, d             byte
	)

	// Move the right pointer to expand the substring and add new characters to
	// the map. If a character appears more than once, move the left pointer to
	// shrink the substring
	for right < len(s) {
		char = s[right]
		dummy[char]++
		right++

		for dummy[char] > 1 {
			d = s[left]
			left++
			dummy[d]--
		}
		// Check if the current substring is longer than the previous longest
		// substring
		if right-left > maxLen {
			maxLen = right - left
		}
	}

	return maxLen
}

// @lc code=end
