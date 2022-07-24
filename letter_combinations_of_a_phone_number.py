from typing import List


class LetterCombinationsOfAPhoneNumber:
    def letter_combinations(self, digits: str) -> List[str]:
        result = []
        digits_to_char = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(index: int, cur_str: str) -> None:
            if len(cur_str) == len(digits):
                result.append(cur_str)
                return

            for char in digits_to_char[digits[index]]:
                backtrack(index + 1, cur_str + char)
        if digits:
            backtrack(0, '')
        return result
