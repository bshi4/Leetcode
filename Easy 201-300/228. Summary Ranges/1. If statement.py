class Solution:
    def summaryRanges(self, nums):
        res = []
        start = 0
        if not nums:
            return res
        nums.append(nums[-1]+2)
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] != 1:
                if i == start:
                    res.append(str(nums[i]))
                else:
                    res.append('{}->{}'.format(nums[start],nums[i]))
                start = i + 1
        return res
 
nums = [0,1,2,4,5,7]
ans = Solution().summaryRanges(nums)
        