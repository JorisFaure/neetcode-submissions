class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0

        left = 0
        right = 1

        while right < len(prices) :
            if prices[right] < prices[left] :
                left = right
                right = left + 1
            else :
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
                right = right + 1
        return max_profit
        