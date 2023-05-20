import sys
from typing import List


class CoinChange:
    def _coin_change(self, coins: List[int], amount: int) -> int:
        """ Calculate the minimum number of coins required to achieve the amount with the given
        denomination

        Args:
            coins (List[int]): Input denominations that are accepted
            amount (int): Target amount to be achieved

        Returns:
            int: Minimum number of coins to achieve that amount value
        """

        # initialize dp array for index ranging from 0 to 'amount' i.e. (amount + 1) blocks
        dp = [amount + 1] * (amount + 1)
        # number of coins needed to get 0 amount = 0
        dp[0] = 0
        # generate min coins for all amounts from 1 to 'amount'
        for amount in range(1, amount + 1):
            # check number of coins needed by considering every denomination we have
            for coin in coins:
                # assign minimum number of coins to that amount
                if (amount - coin) >= 0:
                    dp[amount] = min(dp[amount], 1 + dp[amount - coin])
        return dp[amount] if dp[amount] != (amount + 1) else -1

    def process(self, input_coins: List[int], input_amount: int) -> None:
        print(f"\nInput: \n\tInput denominations: {input_coins}\n\tTarget amount: {input_amount}")
        print(f"\nOutput:\n\t{self._coin_change(input_coins, input_amount)}\n")


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        CoinChange().process([1, 2, 5], 11)
    else:
        number_of_coins = int(input("Enter number of coins: "))
        input_denominations = []
        for index in range(number_of_coins):
            input_denominations.append(int(input(f"Enter denomination {index + 1}: ")))
        target = int(input("Enter target amount: "))
        CoinChange().process(input_denominations, target)