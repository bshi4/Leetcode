from collections import Counter
class Solution:
    def canConstruct(self, ransomNote, magazine):
        ct_ransom = Counter(ransomNote)
        ct_magazine = Counter(magazine)
        for key in ransomNote:
            if ct_ransom[key] > ct_magazine[key]:
                return False
        return True
                
ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
ans = Solution().canConstruct(ransomNote, magazine)
