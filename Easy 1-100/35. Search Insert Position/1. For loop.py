class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
            else:
                return len(nums)+1
        