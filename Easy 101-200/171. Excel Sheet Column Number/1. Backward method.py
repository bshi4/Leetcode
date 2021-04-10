class Solution:
    def titleToNumber(self, columnTitle):
        round = 0
        res = 0
        col = columnTitle
        while col:
            res += (ord(col[-1])-64) * 26**round
            round += 1
            col = col[:-1]
        return res

columnTitle = "ZY"
a = Solution().titleToNumber(columnTitle)
        