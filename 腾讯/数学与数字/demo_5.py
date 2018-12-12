#!/usr/bin/env python
# encoding: utf-8
# @time: 2018-12-11 22:03
# @author: ProYuan
# @Software: PyCharm
"""
2的幂
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:

输入: 1
输出: true
解释: 20 = 1
示例 2:

输入: 16
输出: true
解释: 24 = 16
示例 3:

输入: 218
输出: false
"""


class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 4294967296 % n == 0


if __name__ == '__main__':
    print(Solution().isPowerOfTwo(3))
