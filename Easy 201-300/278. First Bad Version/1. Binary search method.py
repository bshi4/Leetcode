# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        l = 1
        r = n
        while l<r:
            mid = (l+r)//2
            if isBadVersion(mid) is True:
                r = mid
            else:
                l = mid + 1
        return l