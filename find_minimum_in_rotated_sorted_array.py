from typing import List


class FindMinimumInRotatedSortedArray:
    def find_min(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[left] <= nums[right]:
            return nums[left]
        mid = (right + left) // 2
        if nums[mid] >= nums[left]:
            while mid <= right and nums[mid] >= nums[left]:
                mid += 1
            return nums[mid]
        else:
            while mid >= left and nums[mid] <= nums[right]:
                mid -= 1
            return nums[mid + 1]


nums_list = [3, 4, 5, 1, 2]
print(FindMinimumInRotatedSortedArray().find_min(nums_list))
