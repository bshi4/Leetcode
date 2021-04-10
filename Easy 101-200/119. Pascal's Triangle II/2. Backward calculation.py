class Solution:
    def getRow(self, rowIndex):
        result = [1] + [0]*rowIndex
        for i in range(rowIndex):
            for j in range(i+1, 0, -1):
                result[j] += result[j-1]
        return result
    
class Solution1:
    def getRow(self, rowIndex):
        res = [1]
        for i in range(rowIndex):
            for j in range(i, 0, -1):
                res[j] += res[j-1]
            res.append(1)
        return res