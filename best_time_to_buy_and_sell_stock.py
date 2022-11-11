from typing import List


class BestTimeToBuyAndSellStock:
    def _max_profit(self, prices: List[int]) -> int:
        # initialize profit to 0
        profit = 0
        # initialize left pointer to point at the 0th index of the prices list
        left = 0
        # right pointer will range from 1st index of the prices list to the last index of the list
        for right in range(1, len(prices)):
            # only consider prices such that prices pointed by right >= prices pointed by left
            # check above condition
            if prices[right] < prices[left]:
                # if right price is less than left price then right = left (because we found a cheaper price to buy)
                left = right
            # profit is the max value of the price diff between right and left pointer
            profit = max(profit, prices[right] - prices[left])
        return profit

    def process(self, prices: List[int]):
        print(f"\nOutput >> {self._max_profit(prices)}\n")


if __name__ == '__main__':
    list_size = int(input("Enter price list size: "))
    print("Enter prices: ")
    price_list = []
    for element in range(list_size):
        price_list.append(int(input()))
    BestTimeToBuyAndSellStock().process(price_list)
