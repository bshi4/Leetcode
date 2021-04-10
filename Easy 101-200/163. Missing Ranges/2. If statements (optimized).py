class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    def findMissingRanges(self, nums, lower, upper):
        res = []    
        low = lower-1
        nums.append(upper+1)
        for num in nums:
            diff = num-low
            if diff == 2:
                res.append(str(low+1))
            elif diff > 2:
                res.append('{}->{}'.format(low+1, num-1))
            low = num
        return res
