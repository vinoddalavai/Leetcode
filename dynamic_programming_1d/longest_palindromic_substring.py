import sys


class LongestPalindromicSubstring:
    def _longest_palindrome(self, input_string: str) -> str:
        """ Find the longest palindrome in the input string

        Args:
            input_string (str): String in which we have to find the longest palindrome substring

        Returns:
            str: The substring that forms the longest palindrome in the input string
        """

        result, result_length = '', 0
        # consider letter at every index to be the middle of the substring and find palindrome spanning out from the
        # middle
        for index in range(len(input_string)):
            # check for odd length palindrome substring
            left, right = index, index
            # pointers are within array bounds and substring between the pointers is a palindrome
            while left >= 0 and right < len(input_string) and input_string[left] == input_string[right]:
                if (right - left + 1) > result_length:
                    result = input_string[left : right + 1]
                    result_length = right - left + 1
                left -= 1
                right += 1
            # check for even length palindrome substring
            left, right = index, index + 1
            # pointers are within array bounds and substring between the pointers is a palindrome
            while left >= 0 and right < len(input_string) and input_string[left] == input_string[right]:
                if (right - left + 1) > result_length:
                    result = input_string[left : right + 1]
                    result_length = right - left + 1
                left -= 1
                right += 1
        return result
    
    def process(self, input_string: str) -> None:
        print(f"\nInput: \n\tString: {input_string}")
        print(f"\nOutput:\n\t{self._longest_palindrome(input_string)}\n")


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        LongestPalindromicSubstring().process('babad')
    else:
        input_string = input("Enter the input string: ")
        LongestPalindromicSubstring().process(input_string)