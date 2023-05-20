import sys
from typing import List


class WordBreak:
    def _word_break(self, input_string: str, word_dictionary: List[str]) -> bool:
        """ Check if input string contains the word from the dictionary

        Args:
            input_string (str): Word to be checked
            word_dictionary (List[str]): List of words against which we should check the input string

        Returns:
            bool: True if word exists, False otherwise
        """
        # initialize dp array where every index position represents True/False for presence of one of the words in the
        # dictionary starting at that index position
        dp = [False] * (len(input_string) + 1)
        # Assuming that the last index position in the dp array is True
        dp[len(input_string)] = True
        # For every word in the dictionary check to see if that word exists in the input string
        for index in range(len(input_string) - 1, -1, -1):
            for word in word_dictionary:
                # if word is found in the input string then dp value at that starting index is set to whatever value 
                # exists at the index position after the lentgth of the found word
                if (index + len(word) <= len(input_string) and input_string[index : index + len(word)] == word):
                    dp[index] = dp[index + len(word)]
                # if word is found then there is no need to check other words in the dictionary. We can break from the 
                # loop and find other words at the next index position
                if dp[index]:
                    break
        return dp[0]

    def process(self, input_string: str, input_dictionary: List[str]) -> None:
        print(f"\nInput: \n\tInput string: {input_string}\n\tInput dictionary: {input_dictionary}")
        print(f"\nOutput:\n\t{self._word_break(input_string, input_dictionary)}\n")


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        WordBreak().process("applepenapple", ["apple","pen"])
    else:
        input_string = input("Enter the target string: ")
        count = int(input("Enter size of the dictionary: "))
        input_dictionary = []
        for index in range(count):
            input_dictionary.append(input(f"Enter string at {index + 1}: "))
        WordBreak().process(input_string, input_dictionary)