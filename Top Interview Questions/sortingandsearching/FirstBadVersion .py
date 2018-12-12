"""
First Bad Version
"""
"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while low < high - 1:
            if isBadVersion((int)(low + high) / 2):
                high = int(high + low) / 2
            else:
                low = int(low + high) / 2
        if isBadVersion(low):
            return low
        else:
            return high

    def firstBadVersion1(self, n):
        start = 1
        end = n
        while (start < end):
            mid = start + (end - start) / 2
            if not isBadVersion(mid):
                start = mid + 1
            else:
                end = mid

        return start
