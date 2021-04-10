class Solution:
    def countPrimes(self, n):
        count = 0
        for i in range(n):
            if self.isPrime(i):
                count += 1
        return count
            
        
    def isPrime(self, n):
        if n == 0 or n == 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, n):
                if n%i == 0:
                    return False
            return True
        