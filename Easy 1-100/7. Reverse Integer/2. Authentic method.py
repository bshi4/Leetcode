class Solution:
    def reverse(self, x):
        #Authentic method for reverse a number
        val = 0
        temp = x
        while not temp == 0:
            val = val*10 + temp%10
            temp //= 10
        return val

x = 1450
a = Solution().reverse(x)
print(a)