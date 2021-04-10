class Solution:
    def strStr(self, haystack, needle):
        if not needle in haystack:
            return -1
        elif needle == '':
            return 0
        else:
            for i in range(len(haystack)):
                if haystack[i:i+len(needle)] == needle:
                    return i
                
haystack = 'hello'
needle = 'll'
a = Solution().strStr(haystack, needle)
        