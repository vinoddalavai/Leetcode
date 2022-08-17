class PalindromicSubstring:
    def count_substrings(self, s: str) -> int:
        result = 0
        for index in range(len(s)):
            # For odd length substrings
            left = right = index
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1

            # For even length substrings
            left = index
            right = left + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
        return result


input_string = 'aaab'
ps = PalindromicSubstring()
print(f"Number of palindromic substring in the string '{input_string}' = {ps.count_substrings(input_string)}")
