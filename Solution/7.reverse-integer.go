package LeetCode

import "math"

func R(x int) int {
	return reverse(x)
}

/*
 * @lc app=leetcode id=7 lang=golang
 *
 * [7] Reverse Integer
 */

// @lc code=start
func reverse(x int) int {
	var (
		// store the input integer as a 32-bit integer
		source int32 = int32(x)
		// stores the reversed integer as a 32-bit integer
		result int32
		// indicates if the input integer is negative
		isnegative bool
	)

	// check if the input integer is negative, and set the isnegative flag and
	// convert source to positive
	if source < 0 {
		isnegative = true
		source *= -1
	}

	// extract each digit of source by taking the remainder of source divided by
	// 10 construct the reversed integer by multiplying result by 10 and adding
	// each digit in turn check if result is within the range of 32-bit
	// integers, return 0 if not
	for source > 0 {
		if int(result)*10 > math.MaxInt32 {
			return 0
		}
		result = result*10 + source%10
		source /= 10
	}

	// if the input integer was negative, multiply result by -1 before returning
	// it
	if isnegative {
		result *= -1
	}

	return int(result) // cast the result as a 64-bit integer and return it
}

// @lc code=end
