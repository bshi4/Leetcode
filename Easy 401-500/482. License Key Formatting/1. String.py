class Solution:
    def licenseKeyFormatting(self, s, k):
        s = s.replace('-', '').upper()
        a = len(s) % k
        res = ''
        if a != 0:
            res += s[:a]
        while a < len(s):
            if res:
                res += '-' + s[a:a+k]
            else:
                res += s[a:a+k]
            a += k
        return res
            
            
    
s = "5F3Z-2e-9-w"
k = 4
ans = Solution().licenseKeyFormatting(s, k)
