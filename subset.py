from typing import List


class Subset:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, current_subset = [], []

        def dfs(index: int) -> None:
            if index >= len(nums):
                result.append(current_subset.copy())
                return

            # add the current element
            current_subset.append(nums[index])
            dfs(index + 1)

            # do NOT add the current element
            current_subset.pop()
            dfs(index + 1)

        dfs(0)
        return result


if __name__ == '__main__':
    nums_list = [1, 2, 3]
    print("Subsets for the provided set: ")
    print("\t" + str(Subset().subsets(nums_list)))
