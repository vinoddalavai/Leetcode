from typing import List


class LongestConsecutiveSequence:
    def longest_consecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums_set:
                current_longest = 1
                while num + 1 in nums_set:
                    current_longest += 1
                    num += 1
                longest = max(longest, current_longest)
        return longest


nums_list1 = [100, 4, 200, 1, 3, 2]
nums_list2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print("Longest consecutive sequence for " +
      str(nums_list1) + ": " +
      str(LongestConsecutiveSequence().longest_consecutive(nums_list1)))
print("Longest consecutive sequence for " +
      str(nums_list2) + ": " +
      str(LongestConsecutiveSequence().longest_consecutive(nums_list2)))
