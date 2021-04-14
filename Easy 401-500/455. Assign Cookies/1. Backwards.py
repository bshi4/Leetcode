class Solution:
    def findContentChildren(self, g, s):
        g = sorted(g)
        s = sorted(s)
        
        i = len(g)-1
        j = len(s)-1
        count = 0
        
        while min(i, j) >= 0:
            if g[i] <= s[j]:
                count += 1
                j -= 1
            i -= 1
        
        return count
        