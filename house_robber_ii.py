from typing import List


class HouseRobberII:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self._helper(nums[0:len(nums) - 1]), self._helper(nums[1:]))

    def _helper(self, numbers: List[int]):
        rob1, rob2 = 0, 0
        for index in numbers:
            temp = max(index + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


input_nums1 = [2, 3, 2]
input_nums2 = [1, 2, 3, 1]
input_nums3 = [1, 2, 3]
robber = HouseRobberII()
print("Maximum amount that can be robber:")
print(f"\t For input_nums1 = {robber.rob(input_nums1)}")
print(f"\t For input_nums2 = {robber.rob(input_nums2)}")
print(f"\t For input_nums3 = {robber.rob(input_nums3)}")
