package LeetCode

/*
 * @lc app=leetcode id=3 lang=golang
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
func lengthOfLongestSubstring(s string) int {
	var (
		dummy               map[byte]uint8 = make(map[byte]uint8)
		left, right, maxLen int
		char, d             byte
	)

	for right < len(s) {
		char = s[right]
		dummy[char]++
		right++

		for dummy[char] > 1 {
			d = s[left]
			left++
			dummy[d]--
		}
		if right-left > maxLen {
			maxLen = right - left
		}
	}

	return maxLen
}

// @lc code=end
