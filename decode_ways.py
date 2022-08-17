class DecodeWays:
    def num_decodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1
        for index in range(len(s) - 1, -1, -1):
            if s[index] == '0':
                continue
            dp[index] = dp[index + 1]
            if (index + 1) < len(s) and \
                    (s[index] == '1' or
                     (s[index] == '2' and s[index + 1] in '0123456')):
                dp[index] += dp[index + 2]
        return dp[0]


input_string = "2611055971756562"
decode = DecodeWays()
print(f"Number of decodings for the string '{input_string}' = {decode.num_decodings(input_string)}")
