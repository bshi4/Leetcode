class NumArray:

    def __init__(self, nums):
        self.nums1 = [0]
        for num in nums:
            self.nums1.append(self.nums1[-1] + num)
        
        

    def sumRange(self, left, right):
        return self.nums1[right+1] - self.nums1[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)