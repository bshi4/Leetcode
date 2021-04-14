class Solution:
    def findComplement(self, num):
        x = 1
        while x <= num:
            x <<= 1
        return (x-1)^num
        