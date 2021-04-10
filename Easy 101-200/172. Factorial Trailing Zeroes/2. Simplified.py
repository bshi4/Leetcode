class Solution:
    def trailingZeroes(self, n):
        res = 0
        while n != 0:
            res += n//5
            n //= 5
        return res
            
    
n = 1000
a = Solution().trailingZeroes(n)
print(a)
            
        
        