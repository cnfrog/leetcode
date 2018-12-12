"""
Reverse bits of a given 32 bits unsigned integer.

Example:

Input: 43261596
Output: 964176192
Explanation: 43261596 represented in binary as 00000010100101000001111010011100,
             return 964176192 represented in binary as 00111001011110000010100101000000.
Follow up:
If this function is called many times, how would you optimize it?
"""


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans

    def reverseBits1(self, n):
        temp = ((bin(n))[:1:-1])
        temp += "0" * (32 - len(temp))
        return int(temp, 2)

    def reverseBits2(self, n):
        oribin = '{0:032b}'.format(n)
        reversebin = oribin[::-1]
        return int(reversebin, 2)


if __name__ == '__main__':
    n = 43261596
    print(Solution().reverseBits1(n))

