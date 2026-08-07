class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]
        for value in prices :
            maxP = max(maxP, value - minBuy)
            minBuy = min(minBuy, value)
            
        return maxP
            
        