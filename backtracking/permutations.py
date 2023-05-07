from typing import List


class Permutations:
    def _permute(self, nums: List[int]) -> List[List[int]]:
        """ Find all permutations of input list of integers

        Args:
            nums (List[int]): List of integers for which we have to find out
            the permutations

        Returns:
            List[List[int]]: List of permutations for the given input list
        """

        # initialize result list
        result = []

        # base case: return single list element if list size is 1
        if len(nums) == 1:
            return [nums.copy()]

        # iterate through each number in the nums list
        # eg. [1, 2, 3]
        for _ in range(len(nums)):
            # pop first element from nums i.e. 1
            # nums = [2, 3]
            excluded_int = nums.pop(0)
            # recursively call #permute()
            permutations = self._permute(nums)
            # for every permutation in list of permutations add excluded number
            # permutations = [[3, 2, 1], [2, 3, 1]] after for loop
            for permutation in permutations:
                permutation.append(excluded_int)
            # add permutations to result
            result.extend(permutations)
            # add popped number back to initial nums list
            # nums = [2, 3, 1]
            nums.append(excluded_int)
        return result

    def process(self, nums: List[int]) -> List[List[int]]:
        print(f"\nOutput:\n\t{self._permute(nums)}\n")


if __name__ == '__main__':
    Permutations().process([1, 2, 3])