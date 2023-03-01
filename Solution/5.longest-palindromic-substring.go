package LeetCode

func L(s string) string {
	return longestPalindrome(s)
}

/*
 * @lc app=leetcode id=5 lang=golang
 *
 * [5] Longest Palindromic Substring
 */

// @lc code=start
func longestPalindrome(s string) string {
	if len(s) < 1 {
		return ""
	}
	// starting index of the longest palindrome
	var start int
	// ending index of the longest palindrome
	var end int
	// length of the palindrome with i as the center (odd length)
	var len1 int
	// length of the palindrome with i and i+1 as centers (even length)
	var len2 int

	for i := 0; i < len(s); i++ {
		// check for palindrome with i as center
		len1 = expandAroundCenter(s, i, i)
		// check for palindrome with i and i+1 as centers
		len2 = expandAroundCenter(s, i, i+1)
		// if palindrome with i as center is longest so far
		if len1 > len2 && len1 > end-start {
			start = i - len1/2 // update start and end indices
			end = i + len1/2
			continue // continue to next iteration
		}
		// if palindrome with i and i+1 as centers is longest so far
		if len2 > end-start {
			start = i - len2/2 + 1 // update start and end indices
			end = i + len2/2
			continue // continue to next iteration
		}
	}
	return s[start : end+1] // return the longest palindrome substring
}

// function to check for palindrome by expanding around a center index
func expandAroundCenter(s string, left int, right int) int {
	// expand around center while palindrome condition is met
	for left >= 0 && right < len(s) && s[left] == s[right] {
		left--
		right++
	}
	// return the length of the palindrome substring found
	return right - left - 1
}

// @lc code=end
