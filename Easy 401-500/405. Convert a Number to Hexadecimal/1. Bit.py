class Solution:
    def toHex(self, num):
        if num < 0:
            num += 2**32
            
        check = '0123456789abcdef'
        
        res = []
        while num >= 16:
            res.append(check[num%16])
            num //= 16
        res.append(check[num])
        
        return ''.join(res[::-1])