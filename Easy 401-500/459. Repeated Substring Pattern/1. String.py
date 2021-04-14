class Solution:
    def repeatedSubstringPattern(self, s):
        res = ''
        for i in range(len(s)//2):
            res += s[i]
            if res*(len(s)//len(res)) == s:
                return True
        return False