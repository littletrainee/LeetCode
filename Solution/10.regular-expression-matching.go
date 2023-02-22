package LeetCode

/*
 * @lc app=leetcode id=10 lang=golang
 *
 * [10] Regular Expression Matching
 */

// @lc code=start
func isMatch(s string, p string) bool {
	// If pattern is empty
	if len(p) == 0 {
		// Return true only if s is also empty
		return len(s) == 0
	}

	// If pattern ends with '*'
	if p[len(p)-1] == '*' {
		// First, try to match without the character and the '*' Use recursion
		// to compare the remaining s and p.
		return isMatch(s, p[:len(p)-2]) ||
			// If the above failed, then check if the last character of s matches
			// the character before '*' in pattern and that the remaining s matches
			// the same pattern (this is where '*' matches multiple occurrences)
			len(s) > 0 && (p[len(p)-2] == '.' || s[len(s)-1] == p[len(p)-2]) &&
				isMatch(s[:len(s)-1], p)
	}

	// If the last character in pattern matches the last character in s
	if len(s) > 0 && (p[len(p)-1] == '.' || s[len(s)-1] == p[len(p)-1]) {
		// Continue checking the remaining characters
		return isMatch(s[:len(s)-1], p[:len(p)-1])
	}
	return false
}

// @lc code=end
