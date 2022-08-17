class LongestPalindromicSubstring:
    def longest_palindrome(self, s: str) -> str:
        result_length, result = 0, ''
        # For odd length
        for index in range(len(s)):
            left, right = index, index
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > result_length:
                    result_length = right - left + 1
                    result = s[left:right + 1]
                right += 1
                left -= 1

        # For even length
        for index in range(len(s)):
            left, right = index, index + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > result_length:
                    result_length = right - left + 1
                    result = s[left:right + 1]
                right += 1
                left -= 1
        return result


input_string1 = 'babad'
input_string2 = 'cbbd'
longest = LongestPalindromicSubstring()
print("Longest Palindromic Substring: ")
print(f"\t For the string {input_string1} = {longest.longest_palindrome(input_string1)}")
print(f"\t For the string {input_string2} = {longest.longest_palindrome(input_string2)}")
