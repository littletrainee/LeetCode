package LeetCode

/*
 * @lc app=leetcode id=9 lang=golang
 *
 * [9] Palindrome Number
 */

// @lc code=start
func isPalindrome(x int) bool {
	// Check if x is negative, as negative numbers can't be palindromes
	if x < 0 {
		return false
	}

	// Single digit numbers are palindromes
	if x < 10 {
		return true
	}

	// Initialize variables to keep track of reverse and original number
	var (
		reverse int
		temp    int = x
	)

	// Reverse the original number using modulo and division
	for temp != 0 {
		remainder := temp % 10
		temp /= 10
		reverse = reverse*10 + remainder
	}

	// Check if the reverse is equal to the original number
	return reverse == x
}

// @lc code=end
