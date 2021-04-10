class Solution:
    def climbStairs(self, n):
        prev, curr = 0, 1
        for i in range(n):
            prev, curr = curr, prev+curr
        return curr

n = 5
a = Solution().climbStairs(n)