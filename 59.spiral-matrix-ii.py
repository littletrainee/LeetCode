#
# @lc app=leetcode id=59 lang=python
#
# [59] Spiral Matrix II
#


# @lc code=start
class Point:
    def __init__(self, x=0, y=0):
        self.X = x
        self.Y = y


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return [[n]]

        result = []
        for _ in range(n):
            result.append([0] * n)

        current = Point()
        direction = 0
        Left = 0
        Right = len(result[0]) - 1
        Top = 0
        Botton = len(result) - 1

        for i in range(n * n):
            result[current.Y][current.X] = i + 1

            if direction == 0:
                if current.X < Right:
                    current.X += 1
                elif current.X == Right:
                    direction = 1
                    Top += 1
                    current.Y += 1

            elif direction == 1:
                if current.Y < Botton:
                    current.Y += 1
                elif current.Y == Botton:
                    direction = 2
                    current.X -= 1
                    Right -= 1

            elif direction == 2:
                if current.X > Left:
                    current.X -= 1
                elif current.X == Left:
                    direction = 3
                    current.Y -= 1
                    Botton -= 1

            elif direction == 3:
                if current.Y > Top:
                    current.Y -= 1
                elif current.Y == Top:
                    direction = 0
                    current.X += 1
                    Left += 1
        return result


# @lc code=end
