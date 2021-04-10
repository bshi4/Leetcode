class Solution:
    def convertToTitle(self, columnNumber):
        ans = ''
        while columnNumber:
            ans += chr((columnNumber-1)%26+65)
            columnNumber = (columnNumber-1) // 26
        return ans[::-1]
            
            
        

columnNumber = 52
a = Solution().convertToTitle(columnNumber)
        
        