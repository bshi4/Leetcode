class Solution:
    def canConstruct(self, ransomNote, magazine):
        if len(ransomNote) > len(magazine):
            return False
        lookup = {}
        for letter in ransomNote:
            if letter in lookup:
                lookup[letter] += 1
            else:
                lookup[letter] = 1
        
        for letter in magazine:
            if letter in lookup:
                lookup[letter] -= 1
        
        print(lookup)
        
        for i in lookup.values():
            if i > 0:
                return False
        return True
            
ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
ans = Solution().canConstruct(ransomNote, magazine)
