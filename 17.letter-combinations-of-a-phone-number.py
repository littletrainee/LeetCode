#
# @lc app=leetcode id=17 lang=python
#
# [17] Letter Combinations of a Phone Number
#


# @lc code=start

Letter = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        result = []
        self.backtrack("", 0, digits, result)
        return result

    def backtrack(self, combination, index, digits, result):
        if index == len(digits):
            result.append(combination)
            return

        for letter in Letter[digits[index]]:
            self.backtrack(combination + letter, index + 1, digits, result)


# @lc code=end
