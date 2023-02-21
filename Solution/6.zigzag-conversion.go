package LeetCode

/*
 * @lc app=leetcode id=6 lang=golang
 *
 * [6] Zigzag Conversion
 */

// @lc code=start
func convert(s string, numRows int) string {
	// If numRows is less than 2, the string cannot be converted, so return the
	// original string
	if numRows < 2 {
		return s
	}

	var (
		// Create a 2D slice with numRows rows to store the converted string
		sliceholder [][]rune = make([][]rune, numRows)
		// Whether the rows are traversed in reverse order or not
		reverse bool
		// The index of the row currently being traversed
		order int
		// The final converted string
		result []rune
	)

	// Traverse the input string, adding each character to the appropriate row
	// in sliceholder
	for _, v := range s {
		sliceholder[order] = append(sliceholder[order], v)

		// If we are currently traversing the rows in reverse order, move to the
		// previous row
		if reverse {
			order--
		} else { // Otherwise, move to the next row
			order++
		}

		// If we have reached the last row, start traversing the rows in reverse
		// order
		if order == numRows-1 {
			reverse = true
		}

		// If we have reached the first row, start traversing the rows in
		// forward order
		if order == 0 {
			reverse = false
		}
	}

	// Concatenate the characters in each row of sliceholder to create the final converted string
	for _, v := range sliceholder {
		result = append(result, v...)
	}

	// Convert the final result to a string and return it
	return string(result)
}

// @lc code=end
