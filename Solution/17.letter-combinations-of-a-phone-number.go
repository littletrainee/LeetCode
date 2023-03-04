package LeetCode

/*
 * @lc app=leetcode id=17 lang=golang
 *
 * [17] Letter Combinations of a Phone Number
 */

// @lc code=start
// Define a two-dimensional array called "Letter" with 8 rows and
// variable-length columns. Each row represents the letters on a telephone
// keypad for digits 2 to 9
var Letter [8][]byte = [8][]byte{
	{'a', 'b', 'c'}, {'d', 'e', 'f'}, {'g', 'h', 'i'},
	{'j', 'k', 'l'}, {'m', 'n', 'o'}, {'p', 'q', 'r', 's'},
	{'t', 'u', 'v'}, {'w', 'x', 'y', 'z'},
}

func letterCombinations(digits string) []string {
	var result []string
	// Use a switch statement to handle different digit string lengths
	switch len(digits) {
	case 1:
		// For a digit string with length 1, append all the letters associated
		// with that digit to the result slice
		for _, v := range Letter[digits[0]-'2'] {
			result = append(result, string(v))
		}
	case 2:
		// For a digit string with length 2, append all possible letter
		// combinations associated with those digits to the result slice
		for i := 0; i < len(Letter[digits[0]-'2']); i++ {
			for j := 0; j < len(Letter[digits[1]-'2']); j++ {
				result = append(result, string(Letter[digits[0]-'2'][i])+
					string(Letter[digits[1]-'2'][j]))
			}
		}
	case 3:
		// For a digit string with length 3, append all possible letter
		// combinations associated with those digits to the result slice
		for i := 0; i < len(Letter[digits[0]-'2']); i++ {
			for j := 0; j < len(Letter[digits[1]-'2']); j++ {
				for k := 0; k < len(Letter[digits[2]-'2']); k++ {
					result = append(result, string(Letter[digits[0]-'2'][i])+
						string(Letter[digits[1]-'2'][j])+
						string(Letter[digits[2]-'2'][k]))
				}
			}
		}
	case 4:
		// For a digit string with length 4, append all possible letter
		// combinations associated with those digits to the result slice
		for i := 0; i < len(Letter[digits[0]-'2']); i++ {
			for j := 0; j < len(Letter[digits[1]-'2']); j++ {
				for k := 0; k < len(Letter[digits[2]-'2']); k++ {
					for l := 0; l < len(Letter[digits[3]-'2']); l++ {
						result = append(result,
							string(Letter[digits[0]-'2'][i])+
								string(Letter[digits[1]-'2'][j])+
								string(Letter[digits[2]-'2'][k])+
								string(Letter[digits[3]-'2'][l]))
					}
				}
			}
		}
	}
	// Return the result slice
	return result
}

// @lc code=end
