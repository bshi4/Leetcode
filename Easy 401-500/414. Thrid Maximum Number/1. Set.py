class Solution:
    def thirdMax(self, nums):
        a = set(nums)
        if len(a)<3:
            return max(a)
        x = float('-inf')
        y = float('-inf')
        z = float('-inf')
        
        for i in a:
            if i > x:
                z = y
                y = x
                x = i
            elif i > y:
                z = y
                y = i
            elif i > z:
                z = i
        return z
            
        
nums = [3,2,1]
ans = Solution().thirdMax(nums)