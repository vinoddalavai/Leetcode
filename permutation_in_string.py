class PermutationInString:
    def check_inclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_list = [0] * 26
        s2_list = [0] * 26
        for index in range(len(s1)):
            s1_list[ord(s1[index]) - ord('a')] += 1
            s2_list[ord(s2[index]) - ord('a')] += 1

        matches = 0
        for count in range(26):
            if s1_list[count] == s2_list[count]:
                matches += 1

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            ord_value = ord(s2[right]) - ord('a')
            s2_list[ord_value] += 1
            if s2_list[ord_value] == s1_list[ord_value]:
                matches += 1
            elif s2_list[ord_value] == 1 + s1_list[ord_value]:
                matches -= 1

            ord_value = ord(s2[left]) - ord('a')
            s2_list[ord_value] -= 1
            if s2_list[ord_value] == s1_list[ord_value]:
                matches += 1
            elif 1 + s2_list[ord_value] == s1_list[ord_value]:
                matches -= 1
            left += 1
        return matches == 26


string1, string2 = "ab", "eidbaooo"
string3, string4 = "ab", "eidbtaooo"
print("Permutation of string1 '" + string1 + "' in string '" + string2 + "': " +
      str(PermutationInString().check_inclusion(string1, string2)))
print("Permutation of string1 '" + string3 + "' in string '" + string4 + "': " +
      str(PermutationInString().check_inclusion(string3, string4)))
