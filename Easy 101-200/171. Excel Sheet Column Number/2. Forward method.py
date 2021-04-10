class Solution:
    def titleToNumber(self, columnTitle):
        res = 0
        col = columnTitle
        for letter in col:
            res *= 26
            res += ord(letter)-64
        return res

columnTitle = "ZY"
a = Solution().titleToNumber(columnTitle)
        