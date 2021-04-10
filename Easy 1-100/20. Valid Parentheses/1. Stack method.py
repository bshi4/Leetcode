class Solution:
    def isValid(self, s):
        dict1 = {'(':')', '[':']', '{':'}'}
        stack = []
        for item in s:
            if item in dict1.keys():
                stack.append(item)
            elif len(stack) == 0 or item != dict1[stack.pop()]:
                return False
        return len(stack) == 0

s = "()[]{}"
b = Solution().isValid(s)
