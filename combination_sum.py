from typing import List


class CombinationSum:
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        result, current_subset = [], []

        def dfs(index: int, total: int) -> None:
            if total == target:
                result.append(current_subset.copy())
                return
            if index >= len(candidates) or total > target:
                return

            current_subset.append(candidates[index])
            dfs(index, total + candidates[index])
            current_subset.pop()
            dfs(index + 1, total)

        dfs(0, 0)
        return result


nums_list, tar = [2, 3, 6, 7], 7
print("Combination sum:")
print("\t" + str(CombinationSum().combination_sum(nums_list, tar)))
