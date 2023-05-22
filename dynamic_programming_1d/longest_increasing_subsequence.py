import sys
from typing import List


class LongestIncreasingSubsequence:
    def _length_of_list(self, numbers: List[int]) -> int:
        """ Find longest subsequence on increasing numbers in the given input list

        Args:
            numbers (List[int]): List of numbers to find the subsequence

        Returns:
            int: Length of the longest increasing subsequence found in the input list
        """
        # initialize dp to keep track of maximum subsequence for every number in the input array
        # 1 is assigned initially because every number is a subsequence by itself
        dp = [1] * len(numbers)
        # start at the second last index as the last number will have a maximum subsequence of 1
        for i in range(len(numbers) - 2, -1, -1):
            # check value at index 'i' with every other number after it in the input list
            for j in range(i + 1, len(numbers)):
                # for every number at index 'i' check to see if it is less than 'j' value and if so retain the max value
                if numbers[i] < numbers[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)

    def process(self, input_numbers: List[int]) -> None:
        print(f"\nInput: \n\tInput numbers: {input_numbers}")
        print(f"\nOutput:\n\t{self._length_of_list(input_numbers)}\n")


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        LongestIncreasingSubsequence().process([10, 9, 2, 5, 3, 7, 101, 18])
    else:
        count = int(input("Enter size of the list: "))
        input_numbers = []
        for index in range(count):
            input_numbers.append(int(input(f"Enter number at {index + 1}: ")))
        LongestIncreasingSubsequence().process(input_numbers)