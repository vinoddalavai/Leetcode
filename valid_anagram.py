class ValidAnagram:
    def is_anagram_using_map(self, s: str, t: str) -> bool:
        char_map = {}
        for char in s:
            char_map[char] = 1 + char_map.get(char, 0)
        for char in t:
            char_map[char] = char_map.get(char, 0) - 1
        for count in char_map.values():
            if count != 0:
                return False
        return True

    def is_anagram_using_list(self, s: str, t: str) -> bool:
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1
        for char in t:
            freq[ord(char) - ord('a')] -= 1
        for count in freq:
            if count != 0:
                return False
        return True


string1, string2 = "anagram", "nagaram"
string3, string4 = "rat", "car"
print("Using hash map:")
print(ValidAnagram().is_anagram_using_map(string1, string2))
print(ValidAnagram().is_anagram_using_map(string3, string4))
print()
print("Using list:")
print(ValidAnagram().is_anagram_using_list(string1, string2))
print(ValidAnagram().is_anagram_using_list(string3, string4))
