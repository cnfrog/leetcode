'''
9. 回文数
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)

    def isPalindrome1(self, x):
        if x < 0: return False
        l = list()
        while x != 0:
            l.append(x % 10)
            x = x // 10
        return l[::-1] == l

    def isPalindrome2(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x = x // 10
        return revertedNumber == x or revertedNumber // 10 == x


a = Solution().isPalindrome2(121)
print(a)
