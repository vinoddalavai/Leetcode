from typing import List


class CoinChange:
    def coin_change(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for index in range(1, len(dp)):
            for coin in coins:
                if index - coin >= 0:
                    dp[index] = min(dp[index], 1 + dp[index - coin])
        return dp[amount] if dp[amount] != amount + 1 else -1


input_coins, input_amount = [1, 2, 5], 11
cc = CoinChange()
print(f"Minimum number of coins for the given input amount = {cc.coin_change(input_coins, input_amount)}")
