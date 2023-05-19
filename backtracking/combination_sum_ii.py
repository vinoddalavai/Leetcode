import sys

from typing import List


class CombinationSumII:
    def _combination_sum_ii(self,
                            candidates: List[int],
                            target: int) -> List[List[int]]:
        """Finds combination of integers that result in the target value

        Args:
            candidates (List[int]): List of integers from where combination needs to be calcualted
            target (int): Target integer value to be achieved by summing integers from input list

        Returns:
            List[List[int]]: List of combinations that result in the target value
        """

        result = []
        candidates.sort()

        def dfs(index: int, current_subset: List[int], total: int) -> None:
            """DFS starting at given index 
            
            Args:
                index (int): Description
                current_subset (List[int]): Description
                total (int): Description
            
            Returns:
                None: Description
            """
            if total == target:
                result.append(current_subset.copy())
                return
            if total > target or index >= len(candidates):
                return
            current_subset.append(candidates[index])
            dfs(index + 1, current_subset, total + candidates[index])
            current_subset.pop()
            while index + 1 < len(candidates) and \
                    candidates[index] == candidates[index + 1]:
                index += 1
            dfs(index + 1, current_subset, total)

        dfs(0, [], 0)
        return result

    def process(self, candidates: List[int], target: int) -> None:
        print(f"\nInput: \n\tcandidates: {candidates}\ttarget: {target}")
        print(f"\nOutput:\n\t{self._combination_sum_ii(candidates, target)}\n")


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        CombinationSumII().process([1, 2, 2, 5], 5)
    else:
        list_length = int(input('Enter length of input list: '))
        input_target = int(input('Enter target value: '))
        input_list = []
        print()
        for index in range(list_length):
            input_list.append(int(input(
                f"Enter the value for index {index + 1}: ")))
        CombinationSumII().process(input_list, input_target)
