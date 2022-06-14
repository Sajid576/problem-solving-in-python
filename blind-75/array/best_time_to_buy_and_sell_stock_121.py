from typing import List
from my_test import test


def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    min_buy = 100000
    for price in prices:
        if(price < min_buy):
            min_buy = price
        if(price-min_buy > max_profit):
            max_profit = price-min_buy
    return max_profit


test(maxProfit([7, 1, 5, 3, 6, 4]), 5)
test(maxProfit([7, 6, 4, 3, 1]), 0)
