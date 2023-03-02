package LeetCode

import "strings"

/*
 * @lc app=leetcode id=14 lang=golang
 *
 * [14] Longest Common Prefix
 */

// @lc code=start
func longestCommonPrefix(strs []string) string {
	// if the input slice is empty, return an empty string
	if len(strs) == 0 {
		return ""
	}

	// initialize a strings.Builder to store the common prefix, and a byte
	// variable to store the current letter being compared
	var (
		prefix strings.Builder
		letter byte
	)

	// iterate through each letter in the first string in the slice
	for i := 0; i < len(strs[0]); i++ {
		// set the letter to the current letter in the first string
		letter = strs[0][i]
		// iterate through each string in the slice except the first one
		for j := 1; j < len(strs); j++ {
			// if we have reached the end of a string or if the current letter
			// being compared is not equal to the letter in the first string at
			// the same position, return the current common prefix
			if i == len(strs[j]) || strs[j][i] != letter {
				return prefix.String()
			}
		}
		// if the letter is common to all strings, add it to the prefix
		prefix.WriteByte(letter)
	}

	// return the final common prefix
	return prefix.String()
}

// @lc code=end
