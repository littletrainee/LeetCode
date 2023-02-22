package LeetCode

import (
	"math"
	"unicode"
)

/*
 * @lc app=leetcode id=8 lang=golang
 *
 * [8] String to Integer (atoi)
 */

// @lc code=start

func myAtoi(s string) int {
	var (
		result     int // initialize result as 0
		isnegative bool
		started    bool
	)

	for _, v := range s {
		// check if the character is a digit
		if unicode.IsDigit(v) {
			started = true
			digit := int(v - '0')      // convert the character to a digit
			result = result*10 + digit // add the digit to the result
			// check if the result is out of range
			if !isnegative && result > math.MaxInt32 {
				return math.MaxInt32
			}
			if isnegative && -result < math.MinInt32 {
				return math.MinInt32
			}
		} else if v == '+' && !started {
			started = true
		} else if v == '-' && !started {
			started = true
			isnegative = true
		} else if v != ' ' || started {
			// exit the loop if non-space character is encountered after the
			// start
			break
		}
	}

	if isnegative {
		result *= -1
	}

	return result
}

// @lc code=end
