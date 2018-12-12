# -*- coding: utf-8 -*-
# @Time    : 2018/12/1 9:16
# @Author  : ProYuan

"""
字符串转换整数 (atoi)
请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0。

说明：

假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，qing返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

示例 1:

输入: "42"
输出: 42
示例 2:

输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
示例 3:

输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
示例 4:

输入: "words and 987"
输出: 0
解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
     因此无法执行有效的转换。
示例 5:

输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
     因此返回 INT_MIN (−231) 。
"""


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # 导入正则模块
        import re
        # 字符串中查找全部符合条件的整数，返回的是列表，第一个参数是正则，第二个参数是字符串
        # strip()字符串去空格
        ret = re.findall(r"^[-+]?\d+", str.strip())
        # 判断是否有匹配的值，没有的话返回0，例如"word values 987"，匹配不到，返回0
        if ret:
            ret_str = ret[0]  # 匹配的数字的字符串
            ret_str2 = ""  # 记录去符号的字符串，ret_str后面还要使用，所以定义一个新的变量记录
            # 判断是否带有符号 + or -
            if ret_str[0] == "-" or ret_str[0] == "+":
                ret_str2 = ret_str[1:]
            else:
                ret_str2 = ret_str
            # str转int
            ret_int = int(ret_str2)
            # 判断第一个字符是否为负号
            if ret_str[0] == "-":
                # 三目运算符，判断是否溢出
                # 如果ret_int <= 2**31则返回-ret_int，否则返回-2**31
                return -ret_int if ret_int <= 2 ** 31 else -2 ** 31
            else:
                return ret_int if ret_int < 2 ** 31 else 2 ** 31 - 1
        else:
            return 0

    def myAtoi1(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re

        pattern = r"[\s]*[+-]?[\d]+"
        match = re.match(pattern, str)
        if match:
            res = int(match.group(0))
            if res > 2 ** 31 - 1:
                res = 2 ** 31 - 1
            if res < - 2 ** 31:
                res = - 2 ** 31
        else:
            res = 0
        return res


if __name__ == '__main__':
    str = "  -+33"
    print(Solution().myAtoi(str))
