import sys


class DecodeWays:
    def _num_decodings(self, input_string: str) -> int:
        """ Find the number of ways a given string of digits can be decoded to letters

        Args:
            input_string (str): Input string of digits to find permutations of decodings

        Returns:
            int: Number of possible decodings for the given input string
        """
        # initialize dp array to be one more than the string. 
        dp = [0] * (len(input_string) + 1)
        # assign value of '1' to the last index of dp array
        dp[len(input_string)] = 1
        
        #iterate through string in reverse
        for index in range(len(input_string) - 1, -1, -1):
            # since 0 has no mapping, there are no ways of interpreting it
            if input_string[index] == '0':
                dp[index] = 0
            else:
                # consider just the number at this index, then the combinations of the remaining of the number after
                # this index is
                dp[index] = dp[index + 1]
            
            # if current number is a '1' followed by any number or a '2' followed by numbers ranging from 0 to 6 then
            # consider these two numbers as a combination. In that case the number of combinations possible after the 
            # index + 1 number is
            if (index + 1 < len(input_string) and
                (input_string[index] == '1' or
                 (input_string[index] == '2' and input_string[index + 1] in '0123456')
                )):
                dp[index] += dp[index + 2]

        return dp[0]

    def process(self, input_string: str) -> None:
        print(f"\nInput: \n\tString: {input_string}")
        print(f"\nOutput:\n\t{self._num_decodings(input_string)}\n")


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        DecodeWays().process('226')
    else:
        input_string = input("Enter the input string: ")
        DecodeWays().process(input_string)