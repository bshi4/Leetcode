class Solution:
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        while n > 1:         
            if n%2 != 0:
                return False
            else:
                if n == 1:
                    return True
                n //= 2

n = 3
ans = Solution().isPowerOfTwo(n)
        