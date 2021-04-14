class Solution:
    def addStrings(self, num1, num2):
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        l1 = len(num1)
        l2 = len(num2)
        
        if l1 > l2:
            num2 += '0'*(l1-l2)
        else:
            num1 += '0'*(l2-l1)
        
        res = ''
        carry = 0
        for i in range(max(l1, l2)):
            a = int(num1[i]) + int(num2[i]) + carry
            res += str(a%10)
            if a >= 10:
                carry = 1
            else:
                carry = 0
        if carry == 1:
            res += '1'
        
        return res[::-1]
        