import sys
from typing import List


class PartitionEqualSubsetSum:
    def _can_partition(self, nums: List[int]) -> bool:
        """ Check if there exists a subset partition such that they sum up to the same value

        Args:
            nums (List[int]): List of integers to check for subset partition

        Returns:
            bool: True if partition exists and False otherwise
        """
        # if target is odd there cannot be an equal partition
        if sum(nums) % 2:
            return False
        # initialize dp set which will contains all possible summations
        dp = set()
        # add 0 as an element. This is the case when no elements are chosen
        dp.add(0)
        # if we can find half the sum with a set of numbers then it is obvious that the other half can be added up with
        # the remaining numbers
        target = sum(nums) // 2
        # for every element in the set find sum of the index element of nums while iterating over nums in reverse
        # order of iteration has no impact on the result of the program
        for index in range(len(nums) - 1, -1, -1):
            # need tempDP as we cannot change the iterable within the loop
            tempDP = set()
            for element in dp:
                tempDP.add(element + nums[index])
                # add original elements to dp into tempDP
                tempDP.add(element)
            dp = tempDP
        return target in dp

    def process(self, input_numbers: List[int]) -> None:
        print(f"\nInput: \n\tInput numbers: {input_numbers}")
        print(f"\nOutput:\n\t{self._can_partition(input_numbers)}\n")


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        PartitionEqualSubsetSum().process([1, 5, 11, 15])
    else:
        count = int(input("Enter size of the list: "))
        input_numbers = []
        for index in range(count):
            input_numbers.append(int(input(f"Enter number at {index + 1}: ")))
        PartitionEqualSubsetSum().process(input_numbers)