from typing import List


class FindDuplicateNumber:
    def find_duplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow, slow2 = nums[slow], nums[slow2]
            if slow == slow2:
                return slow


numbers = [1, 3, 4, 2, 2]
print("Duplicate number is: " + str(FindDuplicateNumber().find_duplicate(numbers)))
