class Solution:
    def isPalindrome(self, x):
        str_x = str(x)
        a = len(str_x)
        for i in range(a//2):
            if str_x[i] != str_x[a-i-1]:
                return False
        return True

x = -1
b = Solution().isPalindrome(x)
print(b)