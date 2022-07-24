from typing import List


class SubsetsII:
    def subsets_with_dup(self, nums: List[int]) -> List[List[int]]:
        result, subset = [], []
        nums.sort()

        def backtrack(index: int) -> None:
            if index == len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[index])
            backtrack(index + 1)
            subset.pop()
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            backtrack(index + 1)

        backtrack(0)
        return result


input_list = [1, 2, 2, 3]
print("Subsets II: ")
print("\t" + str(SubsetsII().subsets_with_dup(input_list)))
