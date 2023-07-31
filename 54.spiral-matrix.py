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
        direction = "right"
        Left = 0
        Right = len(matrix[0]) - 1
        Top = 0
        Botton = len(matrix) - 1
        result = []

        while len(result) < lineLength:
            result.append(matrix[current.Y][current.X])
            # turn to next

            if direction == "right":
                if current.X < Right:
                    current.X += 1
                elif current.X == Right:
                    direction = "down"
                    Top += 1
                    current.Y += 1

            elif direction == "down":
                if current.Y < Botton:
                    current.Y += 1
                elif current.Y == Botton:
                    direction = "left"
                    current.X -= 1
                    Right -= 1

            elif direction == "left":
                if current.X > Left:
                    current.X -= 1
                elif current.X == Left:
                    direction = "up"
                    current.Y -= 1
                    Botton -= 1

            elif direction == "up":
                if current.Y > Top:
                    current.Y -= 1
                elif current.Y == Top:
                    direction = "right"
                    current.X += 1
                    Left += 1
        return result


# @lc code=end
