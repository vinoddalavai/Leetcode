import sys
from typing import List


class LetterCombinationsOfAPhoneNumber:
    # Map digits to letters as seen on a phone
    MAPPING = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    
    def _letter_combinations(self, digits: str) -> List[str]:
        """ Find all combinations of letters that can be made with the given phone number

        Args:
            digits (str): Phone number for which we have to find combinations

        Returns:
            List[str]: List of all possible combinations that can be made from the input digits
        """

        result = []
        
        def dfs(index: int, combination: str) -> None:
            """DFS implementation of finding letter combinations given a starting index

            Args:
                index (int): Starting index for DFS
                combination (str): Current combination of letters in the DFS path
            """

            # base case: add combination to result if it of the same length as the input digits
            if len(combination) == len(digits):
                result.append(combination)
                return
            for letter in self.MAPPING[digits[index]]:
                dfs(index + 1, combination + letter)
        
        if digits:
            dfs(0, '')
        return result

    def process(self, input_digits: str) -> None:
        print(f"\nInput: \n\tInput String: {input_digits}")
        print(f"\nOutput:\n\t{self._letter_combinations(input_digits)}\n")


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        LetterCombinationsOfAPhoneNumber().process('23')
    else:
        input_digits = input("Enter the digits of a phone number: ")
        LetterCombinationsOfAPhoneNumber().process(input_digits)