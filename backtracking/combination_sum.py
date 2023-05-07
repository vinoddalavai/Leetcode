from typing import List


class CombinationSum:
    def _combination_sum(self,
                         candidates: List[int],
                         target: int) -> List[List[int]]:
        """Find all combinations of integers in input list that sum up to the
        target value

        Args:
            candidates (List[int]): list of input integers from where we have
            to find the combinations
            target (int): target value to be achieved by summing a subset of
            input list

        Returns:
            List[List[int]]: result list of subsets that sum up to the target
            value
        """

        # initialize result to store the final list of integers
        result = []

        def dfs(index: int, current: List, total: int) -> None:
            """DFS to find out combinations that result in the target value

            Args:
                index (int): index position to execute dfs
                current (List): current list of integers in the dfs trail
                total (int): sum of integers in the current list

            Returns:
                None:
            """

            # base cases
            # when total = target add current list of integers to result and
            # exit recursion stack
            if total == target:
                result.append(current.copy())
                return
            # when total > target or when index is out of bounds exit recursion
            # stack
            if total > target or index >= len(candidates):
                return
            # add integer at current index position to the current list
            current.append(candidates[index])
            # case 1: call dfs on same index after incrementing total value
            dfs(index, current, total + candidates[index])
            # case 2: call dfs on next index i.e. excluding the integer at
            # current index
            current.pop()
            dfs(index + 1, current, total)

        # begin dfs from 0th index with empty current list and total as 0
        dfs(0, [], 0)
        return result

    def process(self, candidates: List[int], target: int) -> None:
        print(f"\nOutput:\n\t{self._combination_sum(candidates, target)}\n")


if __name__ == '__main__':
    list_length = int(input('Enter length of input list: '))
    input_target = int(input('Enter target value: '))
    input_list = []
    print()
    for index in range(list_length):
        input_list.append(int(input(
            f"Enter the value for index {index + 1}: ")))
    CombinationSum().process(input_list, input_target)