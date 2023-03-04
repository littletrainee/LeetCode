package LeetCode

/*
 * @lc app=leetcode id=20 lang=golang
 *
 * [20] Valid Parentheses
 */

// @lc code=start
func isValid(s string) bool {
	var (
		// initialize the stack with the first character of s
		stack []byte = []byte{s[0]}
		// index of the top element in the stack
		top int = 0
	)

	for i := 1; i < len(s); i++ {
		// if the current character is an opening bracket
		if s[i] == '(' || s[i] == '{' || s[i] == '[' {
			stack = append(stack, s[i]) // push it onto the stack
			top++                       // update the top index
			continue                    // continue to the next iteration
		}

		// if there are no opening brackets left on the stack or if the current
		// closing bracket does not match the opening bracket at the top of the
		// stack
		if top < 0 ||
			(s[i] == ')' && stack[top] != '(') ||
			(s[i] == ']' && stack[top] != '[') ||
			(s[i] == '}' && stack[top] != '{') {
			return false // the parentheses are not balanced
		}
		// remove the opening bracket at the top of the stack
		stack = stack[:len(stack)-1]
		// update the top index
		top--
	}
	// if the stack is empty, the parentheses are balanced
	return len(stack) == 0
}

// @lc code=end
