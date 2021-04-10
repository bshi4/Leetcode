class Solution:
    def isPowerOfTwo(self, n):
        return n and (n&(n-1) == 0)

n = 3
ans = Solution().isPowerOfTwo(n)
        