from typing import List


class Subsets:
    def _find_subset(self, nums_list: List[int]) -> List[List[int]]:
        """ Return a list of integer lists that are subsets of the input list
        Accept a list of integers as input and use backtracking to find all
        possible subsets of the the given input list.

        :param nums_list: Input list of integers

        :return: Resulting list of list of integetrs that are subsets of the
        given input list.
        """

        # create a result list to store the final result.
        result = []
        # create a subset to keep track of the current subset
        subset = []

        def dfs(start_index):
            """ Perform dfs to find subsets
            Accept a starting index for the input list and find subsets
            starting from that index position to the end of the list.

            :param start_index: Index from where dfs begins
            :return: None
            """

            # base case: if index is out of bounds, save current subset and
            # return out of the recursion
            if start_index >= len(nums_list):
                # copy() is called on subset. If this is not done, the subset
                # values will change everytime we change subset object.
                result.append(subset.copy())
                return
            # route 1: include the number
            subset.append(nums_list[start_index])
            dfs(start_index + 1)
            # route 2: exclude the number
            subset.pop()
            dfs(start_index + 1)

        # begin dfs starting from the 0th position
        dfs(0)
        return result

    def process(self, input_list: List[int]) -> None:
        print(f"\nOutput:\n\t{self._find_subset(input_list)}\n")


if __name__ == '__main__':
    list_size = int(input('Enter the size of the list: '))
    input_nums = []
    print()
    for index in range(list_size):
        input_nums.append(int(input(
            f"Enter the value for number at index {index + 1}: ")))
    print(f"\n Input list is: {input_nums}")
    Subsets().process(input_nums)
