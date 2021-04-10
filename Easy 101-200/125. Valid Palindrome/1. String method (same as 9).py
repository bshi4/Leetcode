import string

class Solution:
    def isPalindrome(self, s):
        s1 = s.lower()
        s2 = ''
        for char in s1:
            if char in string.ascii_lowercase:
                s2 += char
            if char in '0123456789':
                s2 += char
        a = len(s2)//2
        for i in range(a):
            if s2[i] != s2[len(s2)-i-1]:
                return False
        return True
            

s = "A man, a plan, a canal: Panama"
ans = Solution().isPalindrome(s)
        