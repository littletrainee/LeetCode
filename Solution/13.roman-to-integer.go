package LeetCode

/*
 * @lc app=leetcode id=13 lang=golang
 *
 * [13] Roman to Integer
 */

// @lc code=start
func romanToInt(s string) int {
	// Initialize arrays to map Roman numerals to values
	var roman [7]byte = [7]byte{'I', 'V', 'X', 'L', 'C', 'D', 'M'}
	var value [7]uint16 = [7]uint16{1, 5, 10, 50, 100, 500, 1000}

	// Initialize variables to keep track of sum and previous/current values
	var (
		sum      uint16
		previous uint16
		current  uint16
	)

	// Loop through each character in the input string
	for _, v := range []byte(s) {
		// Find the corresponding value for the current Roman numeral
		for j := 0; j < len(roman); j++ {
			if v == roman[j] {
				current = value[j]
				break
			}
		}

		// Subtract twice the previous value if the current value is greater
		// This handles cases like "IV" (4) and "IX" (9)
		if current > previous {
			sum -= 2 * previous
		}

		// Add the current value to the sum and update previous value
		sum += current
		previous = current
	}

	return int(sum)
}

// @lc code=end
