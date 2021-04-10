class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    def findMissingRanges(self, nums, lower, upper):
        res = []
        if not nums:
            if lower == upper:
                res.append(str(lower))
            else:
                res.append('{}->{}'.format(lower, upper))
            return res
        if nums[0] - lower == 1:
            res.append(str(lower))
        elif nums[0] - lower > 1:
            res.append('{}->{}'.format(lower, nums[0]-1))
        for i in range(1, len(nums)):
            if nums[i]-nums[i-1] == 2:
                res.append(str(nums[i]-1))
            elif nums[i]-nums[i-1] > 2:
                res.append('{}->{}'.format(nums[i-1]+1, nums[i]-1))
        if upper - nums[-1] == 1:
            res.append(str(upper))
        elif upper - nums[-1] > 1:
            res.append('{}->{}'.format(nums[-1]+1, upper))
        return res
      
