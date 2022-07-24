from typing import List


class CombinationSumII:
    def combination_sum_2(self, candidates: List[int], target: int) -> List[List[int]]:
        result, subset = [], []
        candidates.sort()

        def backtrack(index: int, total: int) -> None:
            if total == target:
                result.append(subset.copy())
                return
            if index >= len(candidates) or total > target:
                return

            subset.append(candidates[index])
            backtrack(index + 1, total + candidates[index])
            subset.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            backtrack(index + 1, total)

        backtrack(0, 0)
        return result


input_list, target = [10, 1, 2, 7, 6, 1, 5], 8
print("Combination Sum II: ")
print("\t" + str(CombinationSumII().combination_sum_2(input_list, target)))
