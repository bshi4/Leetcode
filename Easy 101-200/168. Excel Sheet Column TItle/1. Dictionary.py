import string

class Solution:
    def convertToTitle(self, columnNumber):
        d = {0:'Z'}
        ans = ''
        for i in range(1, 27):
            d[i] = string.ascii_uppercase[i-1]
        col = columnNumber
        while col > 26:
            last = col % 26
            if last == 0:
                col -= 26
            ans += d[last]
            col //= 26
        
        ans += d[col]
        return ans[::-1]
            
        

columnNumber = 52
a = Solution().convertToTitle(columnNumber)
        
        