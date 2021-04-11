class Solution:
    def reverseVowels(self, s):
        vowel = 'aeiou'
        string = list(s)
        l = 0
        r = len(s)-1
        while l<r:
            if string[l].lower() not in vowel:
                l += 1
            elif string[r].lower() not in vowel:
                r -= 1
            else:
                string[l], string[r] = string[r], string[l]
                l += 1
                r -= 1
        return ''.join(string)