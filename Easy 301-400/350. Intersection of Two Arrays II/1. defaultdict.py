class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookup = collections.defaultdict(int)
        for i in nums1:
            lookup[i] += 1
        
        res = []
        for i in nums2:
            if lookup[i] > 0:
                res.append(i)
                lookup[i] -= 1
        return res