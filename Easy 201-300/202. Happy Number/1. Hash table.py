class Solution:
    def isHappy(self, n):
        set = {n}
        while n != 1:
            sum = 0
            while n:
                sum += (n%10)**2
                n //= 10
            if sum in set:
                return False
            set.add(sum)
            n = sum
        return True
        