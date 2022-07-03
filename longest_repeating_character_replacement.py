class LongestRepeatingCharacterReplacement:
    def character_replacement(self, s: str, k: int) -> int:
        string_hash = {}
        left = 0
        result = 0
        for right in range(len(s)):
            string_hash[s[right]] = 1 + string_hash.get(s[right], 0)
            while (right - left + 1) - max(string_hash.values()) > k:
                string_hash[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result


string1, k1 = "AABABBA", 1
print(LongestRepeatingCharacterReplacement().character_replacement(string1, k1))