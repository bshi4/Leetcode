class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        m = min(strs)
        n = max(strs)
        i = 0
        while i < min(len(m),len(n)):
            if m[i] != n[i]:
                break
            else:
                i += 1
        return m[:i]

strs = ['ace', 'ab', 'abcd']
a = Solution().longestCommonPrefix(strs)