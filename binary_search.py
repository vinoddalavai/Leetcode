from typing import List


class BinarySearch:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


numbers, target = [-1, 0, 3, 5, 9, 12], 9
print("Index of the target: " + str(BinarySearch().search(numbers, target)))
