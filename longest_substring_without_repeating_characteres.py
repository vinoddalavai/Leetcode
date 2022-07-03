class LongestSubstringWithoutRepeatingCharacters:
    def length_of_longest_substring(self, s: str) -> int:
        removed = 0
        longest = 0
        visited_set = set()
        for index in range(len(s)):
            while s[index] in visited_set:
                visited_set.remove(s[removed])
                removed += 1
            visited_set.add(s[index])
            longest = max(longest, index - removed + 1)
        return longest


string1, string2, string3 = "abcabcbb", "bbbbb", "pwwkew"
print("Longest substring without repeating characters in " + string1 + " = " +
      str(LongestSubstringWithoutRepeatingCharacters().length_of_longest_substring(string1)))
print("Longest substring without repeating characters in " + string2 + " = " +
      str(LongestSubstringWithoutRepeatingCharacters().length_of_longest_substring(string2)))
print("Longest substring without repeating characters in " + string3 + " = " +
      str(LongestSubstringWithoutRepeatingCharacters().length_of_longest_substring(string3)))
