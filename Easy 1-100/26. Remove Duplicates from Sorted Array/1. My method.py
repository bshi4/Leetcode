# Can get the correct answer, but cannot pass LC test
class Solution:
    def removeDuplicates(self, nums):
        new_nums = []
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                new_nums.append(nums[i])
        if nums[-1] > nums[-2]:
            new_nums.append(nums[-1])
        return new_nums
            
nums = [1,1,2,4,4,4,6,7]
a = Solution().removeDuplicates(nums)
        