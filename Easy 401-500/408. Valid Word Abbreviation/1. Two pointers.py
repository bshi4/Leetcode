class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    def validWordAbbreviation(self, word, abbr):
        i = 0
        j = 0
        while i < len(abbr):
            if not abbr[i].isdigit():
                if abbr[i] != word[j]:
                    return False
                else:
                    i += 1
                    j += 1
            else:
                if abbr[i] == '0':
                    return False
                n = ''
                while i < len(abbr) and abbr[i].isdigit():
                    n += abbr[i]
                    i += 1
                j += int(n)
        return j == len(word)