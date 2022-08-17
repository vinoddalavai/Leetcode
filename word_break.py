from typing import List


class WordBreak:
    def word_break(self, s: str, word_dict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for index in range(len(s) - 1, -1, -1):
            for word in word_dict:
                if (index + len(word) <= len(s) and
                        s[index : index + len(word)] == word):
                    dp[index] = dp[index + len(word)]
                    if dp[index]:
                        break
        return dp[0]


input_string1, input_string2 = 'applepenapple', 'catsandog'
word_dict1, word_dict2 = ['apple', 'pen'], ['cats', 'dog', 'sand', 'and', 'cat']
wb = WordBreak()
print(f"Can '{input_string1}' be segmented? -> {wb.word_break(input_string1, word_dict1)}")
print(f"Can '{input_string2}' be segmented? -> {wb.word_break(input_string2, word_dict2)}")
