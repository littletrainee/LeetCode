package LeetCode

/*
 * @lc app=leetcode id=12 lang=golang
 *
 * [12] Integer to Roman
 */

// @lc code=start
// RomanNumerals maps integers to their corresponding Roman numeral symbols.
var RomanNumerals = map[int]string{
	1: "I", 4: "IV", 5: "V", 9: "IX",
	10: "X", 40: "XL", 50: "L", 90: "XC",
	100: "C", 400: "CD", 500: "D", 900: "CM",
	1000: "M",
}

// intToRoman converts an integer to a Roman numeral string.
func intToRoman(num int) string {
	// the current place value of the digit being processed
	var placeValue int = 1
	// the resulting Roman numeral string
	var romanStr string
	for ; num > 0; num /= 10 {
		// extract the current digit and multiply it by the current place value
		var digit int = num % 10 * placeValue
		switch {
		case digit == 9*placeValue:
			// handle the special case where digit equals 9
			romanStr = RomanNumerals[9*placeValue] + romanStr
		case digit >= 5*placeValue:
			// start with the symbol for 5 times the current place value
			var t string = RomanNumerals[5*placeValue]
			// subtract 5 times the current place value from digit
			digit -= 5 * placeValue
			for j := 0; j < digit/placeValue; j++ {
				// add the symbol for 1 times the current place value to the
				// string as many times as needed
				t += RomanNumerals[1*placeValue]
			}
			// add the resulting string to the front of the overall Roman
			// numeral string
			romanStr = t + romanStr
		case digit == 4*placeValue:
			// handle the special case where digit equals 4
			romanStr = RomanNumerals[4*placeValue] + romanStr
		default:
			var t string
			for j := 0; j < digit/placeValue; j++ {
				// add the symbol for 1 times the current place value to the
				// string as many times as needed
				t += RomanNumerals[1*placeValue]
			}
			// add the resulting string to the front of the overall Roman
			// numeral string
			romanStr = t + romanStr
		}
		// move to the next place value (i.e., tens, hundreds, thousands)
		placeValue *= 10
	}
	return romanStr
}

// @lc code=end
