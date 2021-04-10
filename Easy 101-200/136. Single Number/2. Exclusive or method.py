# ^ is exclusive or
class Solution:
    def singleNumber(self, nums):
        ans = 0
        for n in nums:
            ans ^= n
        return ans

nums = [4,1,2,1,2]
a = Solution().singleNumber(nums)
