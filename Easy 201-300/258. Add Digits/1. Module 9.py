class Solution:
    def addDigits(self, num):
        if num < 1:
            return 0
        return (num-1)%9 + 1