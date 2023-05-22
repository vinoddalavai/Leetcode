import sys
from typing import List


class MinCostClimbingStairs:
    def _min_cost_climbing_stairs(self, cost: List[int]) -> int:
        """ Find the minimum cost of climbing up to the top of the stairs starting from 0th or 1st step

        Args:
            cost (List[int]): List of cost where cost[i] represents the ith step

        Returns:
            int: The minimum cost to climb up to the top of the stairs
        """

        # modify cost dp array to show minimum cost at every index position of the array
        for index in range(2, len(cost)):
            # steps can be taken in intervals of 1 or 2 steps
            cost[index] += min(cost[index - 1], cost[index - 2])
        return min(cost[-1], cost[-2])

    def process(self, input_cost: List[int]) -> None:
        print(f"\nInput: \n\tCost array: {input_cost}")
        print(f"\nOutput:\n\t{self._min_cost_climbing_stairs(input_cost)}\n")


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        MinCostClimbingStairs().process([1,100,1,1,1,100,1,1,100,1])
    else:
        number_of_stairs = int(input("Enter the number of stairs: "))
        stairs = []
        for index in range(number_of_stairs):
            stairs.append(int(input(f"Enter cost of step[{index + 1}]: ")))
        MinCostClimbingStairs().process(stairs)