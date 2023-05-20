import sys


class PalindromicSubstring:
    def _count_substrings(self, input_string: str) -> int:
        """ Count the number of substring that are palindromes in the current input string

        Args:
            input_string (str): Input string in which we have to find palindrome substrings

        Returns:
            int: Count of the number of palindromic substrings contained in the input string
        """

        result = 0
        for index in range(len(input_string)):
            # find the count of odd length palindromic substring
            result += self._count_palindromes(input_string, index, index)
            # find the count of even length palindromic substring
            result += self._count_palindromes(input_string, index, index + 1)
        return result
    
    def _count_palindromes(self, input_string: str, left: int, right: int) -> int:
        """ Check palindromic susbtrings and return the count

        Args:
            input_string (str): Input string to find palindromes
            left (int): start index to span out to the left
            right (int): start index to span out to the right

        Returns:
            int: number of palindromes
        """

        count = 0
        while left >= 0 and right < len(input_string) and input_string[left] == input_string[right]:
            count += 1
            left -= 1
            right += 1
        return count

    def process(self, input_string: str) -> None:
        print(f"\nInput: \n\tString: {input_string}")
        print(f"\nOutput:\n\t{self._count_substrings(input_string)}\n")


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        PalindromicSubstring().process('babad')
    else:
        input_string = input("Enter the input string: ")
        PalindromicSubstring().process(input_string)