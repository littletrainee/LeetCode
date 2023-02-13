package main

/*
 * @lc app=leetcode id=3 lang=golang
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
func lengthOfLongestSubstring(s string) int {
	var (
		dummy  map[byte]bool = make(map[byte]bool)
		left   int
		right  int
		maxLen int
		char   byte
		d      byte
	)
	for right < len(s) {
		char = s[right]
		dummy[char] = !dummy[char]
		right++
		for !dummy[char] {
			d = s[left]
			left++
			dummy[d] = !dummy[d]
		}
		if right-left > maxLen {
			maxLen = right - left
		}
	}

	return maxLen
}

// @lc code=end
