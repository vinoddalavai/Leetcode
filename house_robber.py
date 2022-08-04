from typing import List


class HouseRobber:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for index in nums:
            temp = max(index + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


input_nums = [2, 7, 9, 3, 1]
robber = HouseRobber()
print(f"Maximum amount of money that can be robbed: {robber.rob(input_nums)}")
