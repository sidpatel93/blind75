# this problem can be solved by using dynamic programming as well as sliding window.
# Here we will solve this problem using dynamic programming.

from typing import List
# solving by DP
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #  min price to buy. we initialize it to day 1. If we sell on the same day then the profit would be 0.
        min_price_to_buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            # count the max profit on each day and adjust the min prices to buy.
            profit = max(profit, prices[i] - min_price_to_buy)
            min_price_to_buy = min(min_price_to_buy, prices[i])
        return profit