from typing import List


class TwoSumII:
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        result = []
        while left < right:
            sum_of_numbers = numbers[left] + numbers[right]
            if sum_of_numbers == target:
                result.append(left + 1)
                result.append(right + 1)
                return result
            elif sum_of_numbers < target:
                left += 1
            else:
                right -= 1
        return result
