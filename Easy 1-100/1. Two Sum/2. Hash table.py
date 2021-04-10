class Solution:
    def twoSum(self, nums, target):
        # Using dictionary as hash table
        error_message = 'No answer'
        d = {}
        for i in range(len(nums)):
            if target-nums[i] in d:
                return [d[target-nums[i]], i]
            d[nums[i]] = i
        return error_message
                
            
            
nums = [3, 3, 4, 9]
target = 12
a = Solution().twoSum(nums, target)