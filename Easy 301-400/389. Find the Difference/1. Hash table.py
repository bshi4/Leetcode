class Solution:
    def findTheDifference(self, s, t):
        dict = {}
        for letter in t:
            if letter not in dict:
                dict[letter] = 1
            else:
                dict[letter] += 1
        
        for letter in s:
            dict[letter] -= 1
        
        for letter in dict:
            if dict[letter] != 0:
                return letter
        