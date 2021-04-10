class Solution:
    def reverse(self, x):
        x1 = int(str(abs(x))[::-1])
        if x1.bit_length() >= 32:
            return 0
        elif x>=0:
            return x1
        elif x<0:
            return -x1

x = 1450
a = Solution().reverse(x)
print(a)