"""
Naive approach, make all hte paris and return the max difference 
but 2 pointer approach
buy = 0
sell = 1

if sell > buy:
    profit = max(proft, old profit)
else:
    buy = sell
sell += 1

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1

        profit = 0
        while buy < sell and sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = max(prices[sell]- prices[buy], profit)
            else:
                buy = sell
            sell += 1

        return profit
