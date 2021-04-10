class Solution:
    def maxSubArray(self, nums):
        ans = 0
        for i in range(len(nums)):
            for j in range(len(nums)-i):
                if sum(nums[i:i+j+1]) > ans:
                    ans = sum(nums[i:i+j+1])
        return ans

nums = [-2,1,-3,4,-1,2,1,-5,4]
a = Solution().maxSubArray(nums)