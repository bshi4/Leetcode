class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        dict = {}
        for letter in s:
            if letter in dict:
                dict[letter] += 1
            else:
                dict[letter] = 1
        for letter in t:
            if letter in dict:
                dict[letter] -= 1
            else:
                return False
            if dict[letter] < 0:
                return False
        return True
        