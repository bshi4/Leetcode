class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    def isStrobogrammatic(self, num):
        l = 0
        r = len(num)-1
        dict = {'6':'9', '1':'1', '8':'8', '9':'6', '0':'0'}
        if len(num) == 1 and num not in ['1','8','0'] or num[len(num)//2] not in dict:
            return False
        
        while l < r:
            if dict[num[l]] != num[r]:
                return False
            l += 1
            r -= 1
        return True

num = '619'
ans = Solution().isStrobogrammatic(num)