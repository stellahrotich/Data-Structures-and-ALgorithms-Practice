"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""
class Solution(object):
    def best_time_to_buy_and_sell_stock(self, prices):
        profit = 0
        for i in range(len(prices)):
            buy_price = price[i]
            for j in range(i, len(prices)):
                sell_price = prices[j]
                profit = max(profit, sell_price - buy_price)
        return profit


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res, buy_price = 0, prices[0]
        for i in range(len(prices)):
            res = max(res, prices[i] - buy_price)
            buy_price = min(buy_price, prices[i])
        return res
