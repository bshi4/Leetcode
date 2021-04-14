class Solution:
    def arrangeCoins(self, n):
        l = 1
        r = n
        while l <= r:
            mid = (l+r)//2
            val = (mid+1)*mid/2
            if val == n:
                return mid
            elif val < n:
                l = mid + 1
            else:
                r = mid - 1
        return r
        