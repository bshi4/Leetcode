class Solution:
    def nextGreaterElement(self, nums1, nums2):
        res = []
        dict = {}
        for i, j in enumerate(nums2):
            dict[j] = i
        
        for n in nums1:
            index = dict[n]
            while index < len(nums2)-1 and n > nums2[index+1]:
                index += 1
            if index == len(nums2)-1:
                res.append(-1)
            else:
                res.append(nums2[index + 1])
        return res