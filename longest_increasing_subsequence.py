from typing import List


class LongestIncreasingSubsequence:
    def length_of_lis(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for index in range(len(nums) - 1, -1, -1):
            for j in range(index + 1, len(nums)):
                if nums[j] > nums[index]:
                    dp[index] = max(dp[index], 1 + dp[j])
        return max(dp)


input_nums = [10, 9, 2, 5, 3, 7, 101, 18]
lis = LongestIncreasingSubsequence()
print(f"Length of longest increasing subsequence in the input list = {lis.length_of_lis(input_nums)}")
