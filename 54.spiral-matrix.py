#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
#

# @lc code=start


class Point:
    def __init__(self, x=0, y=0):
        self.X = x
        self.Y = y


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        lineLength = 0
        for i in matrix:
            lineLength += len(i)

        current = Point()
        direction = 0
        Left = 0
        Right = len(matrix[0]) - 1
        Top = 0
        Botton = len(matrix) - 1
        result = []

        while len(result) < lineLength:
            result.append(matrix[current.Y][current.X])
            # turn to next

            if direction % 4 == 0:
                if current.X < Right:
                    current.X += 1
                elif current.X == Right:
                    direction += 1
                    Top += 1
                    current.Y += 1

            elif direction % 4 == 1:
                if current.Y < Botton:
                    current.Y += 1
                elif current.Y == Botton:
                    direction += 1
                    current.X -= 1
                    Right -= 1

            elif direction % 4 == 2:
                if current.X > Left:
                    current.X -= 1
                elif current.X == Left:
                    direction += 1
                    current.Y -= 1
                    Botton -= 1

            elif direction % 4 == 3:
                if current.Y > Top:
                    current.Y -= 1
                elif current.Y == Top:
                    direction += 1
                    current.X += 1
                    Left += 1
        return result


# @lc code=end
