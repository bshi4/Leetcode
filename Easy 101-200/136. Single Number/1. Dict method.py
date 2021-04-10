class Solution:
    def singleNumber(self, nums):
        dict1 = {}
        for n in nums:
            if not n in dict1.keys():
                dict1[n] = 1
            else:
                dict1[n] += 1
        for n1 in dict1:
            if dict1[n1] == 1:
                return n1

nums = [4,1,2,1,2]
a = Solution().singleNumber(nums)
