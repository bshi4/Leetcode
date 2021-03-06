class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """
    def generatePossibleNextMoves(self, s):
        res = []
        for i in range(len(s)-1):
            if s[i:i+2] == '++':
                res.append(s[:i]+'--'+s[i+2:])
        return res