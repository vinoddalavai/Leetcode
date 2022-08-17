from typing import List


class MinCostClimbingStairs:
    def min_cost_climbing_stairs(self, cost: List[int]) -> int:
        cost.append(0)
        for index in range(len(cost) - 3, -1, -1):
            cost[index] += min(cost[index + 1], cost[index + 2])
        return min(cost[0], cost[1])


input_cost1 = [10, 15, 20]
input_cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
min_cost = MinCostClimbingStairs()
print("Minimum Cost of Climbing Stairs: ")
print(f"\tFor input_cost1: {min_cost.min_cost_climbing_stairs(input_cost1)}")
print(f"\tFor input_cost2: {min_cost.min_cost_climbing_stairs(input_cost2)}")
