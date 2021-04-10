class Solution:
    def addBinary(self, a, b):
        carry, val = 0, 0
        ans = ''
        for i in range(max(len(a), len(b))):
            val = carry
            if i < len(a):
                val += int(a[-(i+1)])
            if i < len(b):
                val += int(b[-(i+1)])
            carry, val = val // 2, val % 2
            ans += str(val)
        if carry:
            ans += '1'
        return ans[::-1]
            
a = "1010"
b = "1011"         
ans1 = Solution().addBinary(a, b)   