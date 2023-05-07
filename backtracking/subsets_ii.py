from typing import List


class SubsetII:
    def _subsets_with_duplicates(self, nums: List[int]) -> List[List[int]]:
        """Find subsets with duplicates in the input nums list

        Args:
            nums (List[int]): List of integers for which we have to find the
            subsets

        Returns:
            List[List[int]]: All subsets of input nums list
        """

        # initialize result
        result = []
        # sort numbers in ascending order so that all integers of same value
        # will be adjacent to one another
        nums.sort()

        def dfs(index: int, current_subset: List) -> None:
            """ DFS implementation to find subsets from current index position

            Args:
                index (int): index position to begin DFS
                current_subset (List): current subset of integers from nums list

            Returns:
                None:
            """

            # base case: if index is out of bounds add current subset to result
            # and return
            if index >= len(nums):
                result.append(current_subset.copy())
                return
            # Add the number at current index
            current_subset.append(nums[index])
            dfs(index + 1, current_subset)
            current_subset.pop()

            # Don't add the number at current index
            # do not add duplicate numbers to the next subset
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            dfs(index + 1, current_subset)

        # begin DFS from index 0 with empty subset
        dfs(0, [])
        return result

    def process(self, input_list: List[int]) -> None:
        print(f"\nOutput:\n\t{self._subsets_with_duplicates(input_list)}\n")


if __name__ == '__main__':
    list_size = int(input('Enter the size of the list: '))
    input_nums = []
    print()
    for index in range(list_size):
        input_nums.append(int(input(
            f"Enter the value for number at index {index + 1}: ")))
    print(f"\n Input list is: {input_nums}")
    SubsetII().process(input_nums)