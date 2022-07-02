from collections import defaultdict
from typing import List


class GroupAnagrams:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            char_list = [0] * 26
            for char in word:
                char_list[ord(char) - ord('a')] += 1
            result[tuple(char_list)].append(word)
        return result.values()


strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
print("Anagram groups: \n" + str(GroupAnagrams().group_anagrams(strings)))
