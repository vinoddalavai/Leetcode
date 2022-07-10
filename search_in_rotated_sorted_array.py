from typing import List


class SearchInRotatedSortedArray:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if target == nums[mid]:
                return mid

            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


n, t = [4, 5, 6, 7, 0, 1, 2], 0
print("Searching for " + str(t) + " in " + str(n) + "\n" +
      "\tFound at index: " + str(SearchInRotatedSortedArray().search(n, t)))
