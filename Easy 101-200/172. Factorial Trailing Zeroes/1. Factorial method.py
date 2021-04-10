class Solution:
    def trailingZeroes(self, n):
        if n == 0:
            return 0
        def factorial(self, n):
            res = 1
            for i in range(1, n+1):
                res *= i
            return res
        num = str(factorial(self, n))
        count = 0
        for i in range(len(num)-1, -1, -1):
            if num[i] == '0':
                count += 1
            else:
                break
        return count
            
    
n = 1000
a = Solution().trailingZeroes(n)
print(a)
            
        
        