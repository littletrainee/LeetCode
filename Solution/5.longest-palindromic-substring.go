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
	var (
		// Store the longest palindrome substring found so far
		max string
		// Length of the input string
		length int = len(s)
		// Whether the current substring is a palindrome or not
		NoPalindrome bool
	)

	// Loop through all possible substrings
	for start := 0; start < length; start++ {
		for end := length; end > start; end-- {
			// If the length of the longest palindrome found so far is >= the
			// length of the current substring, we can stop checking since there
			// is no way the current substring can be longer than the longest
			// palindrome found so far
			if len(max) >= end-start {
				break
			}

			NoPalindrome = false
			for i := start; i <= (start+end-1)/2; i++ {
				if s[i] != s[end-1-i+start] {
					NoPalindrome = true
					break
				}
			}

			// Check if the current substring is a palindrome and update max if
			// it is
			if !NoPalindrome {
				max = s[start:end]
			}
		}
	}

	return max
}

// @lc code=end
