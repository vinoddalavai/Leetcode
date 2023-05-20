import sys
from typing import List


class MaximumProductSubarray:
    def _max_product(self, numbers: List[int]) -> int:
        """ Find the sub-array that results in the maximum product

        Args:
            numbers (List[int]): Input list of integers to find the sub-array

        Returns:
            int: Maximum product of the sub-array
        """
        # initialize result to have maximum value from nums so that if the input is just a list with one element
        # that would be the max value
        result = max(numbers)
        # initialize current_min and current_max to be '1' each as '1' is a neutral value when finding product of
        # numbers
        current_min, current_max = 1, 1
        for number in numbers:
            # if current number is 0 then we have to reset the current_min and current_max as n * 0 = 0
            if number == 0:
                current_min, current_max = 1, 1
                continue
            # hold current_max in a temp variable as it will be used for current_min as well
            temp_max = number * current_max
            # if number is positive, if number is negative and current_min/max is negative or if number is the largest
            current_max = max(number * current_max, number * current_min, number)
            # if number is positive, if number is negative and current_min/max is negative or if number is the smallest
            current_min = min(temp_max, number * current_min, number)
            result = max(result, current_max)
        return result

    def process(self, input_numbers: List[int]) -> None:
        print(f"\nInput: \n\tInput numbers: {input_numbers}")
        print(f"\nOutput:\n\t{self._max_product(input_numbers)}\n")


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        MaximumProductSubarray().process([2, 3, -2, 4])
    else:
        count = int(input("Enter size of the input list: "))
        input_numbers = []
        for index in range(count):
            input_numbers.append(int(input(f"Enter number {index + 1}: ")))
        MaximumProductSubarray().process(input_numbers)