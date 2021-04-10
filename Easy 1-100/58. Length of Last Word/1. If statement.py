class Solution:
    def lengthOfLastWord(self, s):
        s1 = s.split()
        if s1:
            return len(s1[-1])
        return 0