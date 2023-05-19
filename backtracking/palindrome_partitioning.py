import sys
from typing import List


class PalindromePartitioning:
    def _partition(self, input_string: str) -> List[List[str]]:
        """Find partitions that result in the substrings being palindromes

        Args:
            input_string (str): String input for which we need to find palindrome partitions

        Returns:
            List[List[str]]: All substring from various partitions that are palindromes
        """

        result, partition = [], []
        
        def dfs(index):
            """DFS implementation from an index position which marks the partition for that recursion

            Args:
                index (_type_): Integer value that is the index position for the partition
            """

            # base case: if we reach the end of the string add partition to the result set and return
            if index >= len(input_string):
                result.append(partition.copy())
                return
            # check for palindrome at every position starting from current index position
            for j in range(index, len(input_string)):
                if self._is_palindrome(input_string, index, j):
                    # if substring is a palindrome add it to the partition
                    partition.append(input_string[index : j + 1])
                    # recursively call dfs on the next index position
                    dfs(j + 1)
                    # pop the last added substring from partition
                    partition.pop()
        
        dfs(0)
        return result

    def _is_palindrome(self, input_string: str, left: int, right: int) -> bool:
        """Check if input substring spanning from left index value to right index value is a palindrome

        Args:
            input_string (str): String to check for palindrome substring
            left (int): Starting index value for the substring to be checked
            right (int): Ending index value for the substring to be checked

        Returns:
            bool: True if substring is a palindrome and False otherwise
        """

        while left <= right:
            if input_string[left] == input_string[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

    def process(self, input_string: str) -> None:
        print(f"\nInput: \n\tInput String: {input_string}")
        print(f"\nOutput:\n\t{self._partition(input_string)}\n")


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        PalindromePartitioning().process('aab')
    else:
        input_string = input("Enter a string: ")
        PalindromePartitioning().process(input_string)