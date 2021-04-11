class Solution:
    def isSubsequence(self, s, t):
        if not s:
            return True
        if len(s) > len(t):
            return False
        
        i = 0
        for letter in t:
            if letter == s[i]:
                i += 1
            if i == len(s):
                return True
        
        return False
                
        