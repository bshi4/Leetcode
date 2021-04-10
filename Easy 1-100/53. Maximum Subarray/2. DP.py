class Solution:
    def maxSubArray(self, nums):
        res = cur = nums[0]
        for n in nums[1:]:
            cur = max(cur+n, n)
            res = max(res, cur)
        return res
