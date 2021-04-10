class Solution:
    def maxProfit(self, prices):
        if len(prices) == 1:
            return 0
        profit = []
        for i in range(1, len(prices)):
            profit.append(prices[i]-prices[i-1])
        new_profit = [profit[0]]
        for j in range(1, len(profit)):
            if profit[j] + new_profit[j-1] >= profit[j]:
                new_profit.append(profit[j] + new_profit[j-1])
            else:
                new_profit.append(profit[j])
        return max(max(new_profit),0)
            
        
        
prices = [7,1,5,3,6,4]
a = Solution().maxProfit(prices)


class Solution1:
    def maxProfit(self, prices):
        if len(prices) == 1:
            return 0
        profit = []
        for i in range(1, len(prices)):
            profit.append(prices[i]-prices[i-1])
        res = curr = profit[0]
        for n in profit[1:]:
            curr = max(curr+n, n)
            res = max(curr, res)
        return max(res, 0)