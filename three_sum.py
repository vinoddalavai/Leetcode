from typing import List


class ThreeSum:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for index in range(len(nums)):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            left, right = index + 1, len(nums) - 1
            while left < right:
                sum_of_numbers = nums[index] + nums[left] + nums[right]
                if sum_of_numbers == 0:
                    result.append([nums[index], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif sum_of_numbers < 0:
                    left += 1
                else:
                    right -= 1
        return result


numbers1, numbers2, numbers3 = [-1, 0, 1, 2, -1, -4], [], [0]
print("Three sum result of " + str(numbers1) + " : " +
      str(ThreeSum().three_sum(numbers1)))
print("Three sum result of " + str(numbers2) + " : " +
      str(ThreeSum().three_sum(numbers2)))
print("Three sum result of " + str(numbers3) + " : " +
      str(ThreeSum().three_sum(numbers3)))
