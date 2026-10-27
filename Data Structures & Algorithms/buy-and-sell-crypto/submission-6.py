class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0

        buy_val = prices[0]

        i = 1

        while i  < len(prices) :
            if prices[i] < buy_val :
                buy_val = prices[i]
            max_profit = max(max_profit, prices[i] - buy_val)
            i+=1
        return max_profit
