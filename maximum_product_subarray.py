from typing import List


class MaximumProductSubarray:
    def max_product(self, nums: List[int]) -> int:
        cur_min, cur_max = 1, 1
        result = nums[0]
        for num in nums:
            temp = num * cur_max
            cur_max = max(temp, num * cur_min, num)
            cur_min = min(temp, num * cur_min, num)
            result = max(result, cur_max)
        return result


input_numbers = [2, 3, 0, 3, 4]
mps = MaximumProductSubarray()
print(f"Maximum product of the input list {input_numbers} = {mps.max_product(input_numbers)}")
