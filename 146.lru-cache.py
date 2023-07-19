#
# @lc app=leetcode id=146 lang=python
#
# [146] LRU Cache
#

# @lc code=start
import collections
from collections import OrderedDict


class CustomOrderedDict(OrderedDict):
    def move_to_end(self, key):
        value = self.pop(key)
        self[key] = value


# 在LeetCode的代码中使用CustomOrderedDict代替OrderedDict，它包含了自定义的move_to_end方法。


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = CustomOrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1
        val = self.dic[key]
        self.dic.move_to_end(key)
        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.dic[key] = value
        self.dic.move_to_end(key)
        if len(self.dic) > self.capacity:
            self.dic.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
