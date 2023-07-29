#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#


# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strs_table = {}

        for string in strs:
            sorted_string = "".join(sorted(string))

            if sorted_string not in strs_table:
                strs_table[sorted_string] = []

            strs_table[sorted_string].append(string)

        return list(strs_table.values())


# @lc code=end
