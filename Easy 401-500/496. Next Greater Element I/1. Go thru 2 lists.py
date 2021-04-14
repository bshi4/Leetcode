class Solution:
    def nextGreaterElement(self, nums1, nums2):
        res = []
        flag = 0
        for n in nums1:
            index = nums2.index(n)
            flag = 0
            if index == len(nums2)-1:
                res.append(-1)
            else:
                for i in range(index+1, len(nums2)):
                    if nums2[i] > n:
                        res.append(nums2[i])
                        flag = 1
                        break
                if flag == 0:
                    res.append(-1)
        return res
                    
            

nums1 = [4,1,2]
nums2 = [1,3,4,2]
ans = Solution().nextGreaterElement(nums1, nums2)
                    