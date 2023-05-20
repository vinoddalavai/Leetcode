import sys


class ClimbingStairs:
    def _climb_stairs(self, n: int) -> int:
        """Use dynamic programming to find out number of distinct ways to reach step 'n'

        Args:
            n (int): Integer representing the step to reach

        Returns:
            int: Number of distinct ways to reach the step 'n'
        """

        #guard clause
        if n < 3:
            return n
        # initialize dp array
        dp = [0] * (n+1)
        # base values
        dp[0], dp[1], dp[2] = 0, 1, 2
        # fill dp array based on the previous values
        for step in range(3, n+1):
            dp[step] = dp[step - 1] + dp[step - 2]
        # result is the value at index position 'n' in the dp array
        return dp[n]
    
    def process(self, limit: int) -> None:
        print(f"\nInput: \n\tLimit value: {limit}")
        print(f"\nOutput:\n\t{self._climb_stairs(limit)}\n")


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        ClimbingStairs().process(5)
    else:
        input_limit_value = int(input("Enter a limit value (integer): "))
        ClimbingStairs().process(input_limit_value)