class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        min_price = prices[0]
        for p in prices:
            min_price = min(p, min_price)
            max_profit = max(p-min_price, max_profit)
        return max_profit
            
            
        
        
prices = [7,1,5,3,6,4]
a = Solution().maxProfit(prices)
        
