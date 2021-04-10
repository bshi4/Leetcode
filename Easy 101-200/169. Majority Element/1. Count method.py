class Solution:
    def majorityElement(self, nums):
        index = 0
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[index]:
                count += 1
            else:
                count -= 1
                
            if count == 0:
                index = i
                count = 1
            print(index)
            print(count)
        return nums[index]
        
nums = [8, 8, 7, 7, 7]
a = Solution().majorityElement(nums)