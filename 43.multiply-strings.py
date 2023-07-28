#
# @lc app=leetcode id=43 lang=python
#
# [43] Multiply Strings
#


# @lc code=start
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1[0] == "0" or num2[0] == "0":
            return "0"
        numDictionary = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "0": 0,
        }
        resultInt = []
        n1 = len(num1)
        n2 = len(num2)

        # 建立結果列表
        for _ in range(n1 + n2):
            resultInt.append(0)
        # 逐項迭代每個元素做計算
        for i in reversed(range(n2)):
            for j in reversed(range(n1)):
                # 當前兩個數字的計算結果
                target = numDictionary[num2[i]] * numDictionary[num1[j]]
                smallPosition = n2 - 1 - i + n1 - 1 - j
                midPosition = n2 - 1 - i + n1 - 1 - j + 1
                largePosition = n2 - 1 - i + n1 - 1 - j + 2
                small = target % 10 + resultInt[smallPosition]
                if small >= 10:
                    small -= 10
                    resultInt[midPosition] += 1
                mid = target // 10 + resultInt[midPosition]
                if mid >= 10:
                    mid -= 10
                    resultInt[largePosition] += 1

                resultInt[smallPosition] = small
                resultInt[midPosition] = mid

        resultInt.reverse()
        result = ""
        for i in resultInt:
            for k, v in numDictionary.items():
                if v == i:
                    result += k
        for i in range(len(result)):
            if result[i] != "0":
                result = result[i:]
                break

        return result


# @lc code=end
