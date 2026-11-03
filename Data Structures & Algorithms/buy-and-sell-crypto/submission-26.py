class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for x in prices:
            profit = max(profit, x - buy)
            buy = min(buy, x)
        return profit