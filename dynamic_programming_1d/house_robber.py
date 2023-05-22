import sys
from typing import List


class HouseRobber:
    def _rob(self, nums: List[int]) -> int:
        """ Find the maximum amount that can be robbed from the houses

        Args:
            nums (List[int]): List of integers where the index is the house and the value is the amount that can be
            robbed from that house

        Returns:
            int: Maximum amount that can be robbed from all the houses
        """

        # if there are less than three houses then the house with the maximum amount is robbed as they are adjacent
        # to each other and we cannot rob two adjacent houses
        if len(nums) < 3:
            return max(nums)
        # initialize dp array 
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        # no two adjacent houses can be robbed. Either 'i + (i - 2) or (i - 1)'
        for index in range(2, len(nums)):
            dp[index] = max(nums[index] + dp[index - 2], dp[index - 1])
        # return the cost at the last index of cost array
        return dp[-1]

    def process(self, input_nums: List[int]) -> None:
        print(f"\nInput: \n\tHouses: {input_nums}")
        print(f"\nOutput:\n\t{self._rob(input_nums)}\n")


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        HouseRobber().process([2,7,9,3,1])
    else:
        num_houses = int(input("Enter the number of houses: "))
        houses = []
        for index in range(num_houses):
            houses.append(int(input(f"Enter cost of house[{index + 1}]: ")))
        HouseRobber().process(houses)