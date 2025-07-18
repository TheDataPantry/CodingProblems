from typing import List

def maxProfit(self, prices: List[int]) -> int:
    """
    Set initial buy to first element of list and profit to 0.
    As you go through each day, identify if current price is less than price you purchased
    If the current price - the price you paid is greater than the current profit total, update the profit
    Because profit is only evaluated for days where current price is not less than buy price, able to capture max profit
    """
    buy = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] < buy:
            buy = prices[i]
        elif prices[i] - buy > profit:
            profit = prices[i] - buy
    return profit