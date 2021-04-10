class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    def isStrobogrammatic(self, num):
        dict = {'6':'9', '1':'1', '8':'8', '9':'6', '0':'0'}
        n = len(num)
        for i in range((n+1)//2):
            if num[i] not in dict or dict[num[i]] != num[n-1-i]:
                return False
        return True