class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num
        while l<=r:
            mid = (l+r)//2
            a = mid*mid
            if a == num:
                return True
            elif a < num:
                l = mid+1
            else:
                r = mid-1
        return False