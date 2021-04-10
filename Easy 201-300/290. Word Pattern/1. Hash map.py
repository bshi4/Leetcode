class Solution:
    def wordPattern(self, pattern, s):
        s1 = s.split(' ')
        dict1 = {}
        dict2 = {}
        if len(pattern) != len(s1):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dict1:
                dict1[pattern[i]] = s1[i]
                if s1[i] in dict2:
                    return False
                dict2[s1[i]] = True
            else:
                if dict1[pattern[i]] != s1[i]:
                    return False
        return True
            
            