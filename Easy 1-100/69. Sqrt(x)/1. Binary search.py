class Solution:
    def mySqrt(self, x):
        if x == 1:
            return 1
        low = 0
        high = x
        mid = x//2
        while mid*mid != x:
            if mid*mid > x:
                high = mid
            else:
                low = mid
            mid = (high+low)//2
            if mid == low:
                break
        return mid

x = 1
a = Solution().mySqrt(x)
        