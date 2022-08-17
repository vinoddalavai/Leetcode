from typing import List


class PartitionEqualSubsetSum:
    def can_partition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for index in range(len(nums) - 1, -1, -1):
            temp_dp = set(dp)
            for t in dp:
                if nums[index] + t == target:
                    return True
                temp_dp.add(nums[index] + t)
            dp = temp_dp
        return False
