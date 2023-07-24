#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#


# @lc code=start
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in board:
            check = {}
            for j in i:
                if j != "." and j not in check:
                    check[j] = True
                elif j in check:
                    return False
        clone = []
        # 獲取欄值
        for i in range(len(board)):
            temp = []
            for j in range(len(board)):
                temp.append(board[j][i])
            clone.append(temp)
        for i in clone:
            check = {}
            for j in i:
                if j != "." and j not in check:
                    check[j] = True
                elif j in check:
                    return False
        # 獲取區塊值
        clone = []
        first = []
        second = []
        third = []
        for i in range(len(board)):
            first.extend(board[i][0:3])
            second.extend(board[i][3:6])
            third.extend(board[i][6:9])
            if i == 2 or i == 5 or i == 8:
                clone.append(first)
                clone.append(second)
                clone.append(third)
                first = []
                second = []
                third = []
        for i in clone:
            check = {}
            for j in i:
                if j != "." and j not in check:
                    check[j] = True
                elif j in check:
                    return False
        return True


# @lc code=end
