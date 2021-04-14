class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def validWordSquare(self, words):
        for i in range(len(words)):
            for j in range(len(words[0])):
                if words[i][j] != words[j][i]:
                    return False
        return True