class Solution:
    def romanToInt(self, s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev = 0
        s1 = s[::-1]
        for letter in s1:
            if roman[letter] >= prev:
                total += roman[letter]
            else:
                total -= roman[letter]
            prev = roman[letter]
        return total

s = "IV"
a = Solution().romanToInt(s)
print(a)