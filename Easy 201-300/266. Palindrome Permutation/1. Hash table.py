class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def canPermutePalindrome(self, s):
        dict = {}
        for letter in s:
            if letter in dict:
                dict[letter] += 1
            else:
                dict[letter] = 1
        count = 0
        for key in dict:
            if not dict[key] % 2 == 0:
                count += 1
        return count < 2
