from typing import List


class PalindromePartitioning:
    def partition(self, s: str) -> List[List[str]]:
        result, partition = [], []

        def dfs(index: int):
            if index >= len(s):
                result.append(partition.copy())
                return
            for j in range(index, len(s)):
                if self.is_palindrome(s, index, j):
                    partition.append(s[index:j + 1])
                    dfs(j + 1)
                    partition.pop()

        dfs(0)
        return result

    def is_palindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


input_string = 'babaa'
print("Palindrome partitions: ")
print("\t" + str(PalindromePartitioning().partition(input_string)))
