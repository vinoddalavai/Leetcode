from typing import List


class BestTimeToBuyAndSellStock:
    def max_profit(self, prices: List[int]) -> int:
        cost_price, profit = prices[0], 0
        for index in range(len(prices)):
            if prices[index] > cost_price:
                profit = max(profit, prices[index] - cost_price)
            else:
                cost_price = prices[index]
        return profit


price_list = [7, 1, 5, 3, 6, 4]
print("Maximum profit: " + str(BestTimeToBuyAndSellStock().max_profit(price_list)))
