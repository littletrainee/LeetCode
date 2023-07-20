#
# @lc app=leetcode id=735 lang=python
#
# [735] Asteroid Collision
#


# @lc code=start
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for asteroid in asteroids:
            if not stack or asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0:
                    if stack[-1] + asteroid > 0:
                        break
                    elif stack[-1] + asteroid < 0:
                        stack.pop()
                    else:
                        stack.pop()
                        break
                else:
                    stack.append(asteroid)

        return stack


# @lc code=end
