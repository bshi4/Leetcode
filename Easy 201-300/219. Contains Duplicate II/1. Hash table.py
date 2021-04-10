class Solution:
    def containsNearbyDuplicate(self, nums, k):
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = i
            else:
                if i-dict[nums[i]] <= k:
                    return True
                dict[nums[i]] = i
        return False
                
nums = [1, 0, 1, 1]
k = 1
ans = Solution().containsNearbyDuplicate(nums, k)