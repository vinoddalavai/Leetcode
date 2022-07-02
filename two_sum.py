from typing import List


class TwoSum:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        nums_hash = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in nums_hash:
                return [index, nums_hash[diff]]
            else:
                nums_hash[num] = index
        return []


numbers1, target1 = [2, 7, 11, 15], 9
numbers2, target2 = [3, 2, 4], 6
numbers3, target3 = [3, 3], 7
print("Result of two sum: \n" + str(TwoSum().two_sum(numbers1, target1)))
print()
print("Result of two sum: \n" + str(TwoSum().two_sum(numbers2, target2)))
print()
print("Result of two sum: \n" + str(TwoSum().two_sum(numbers3, target3)))
