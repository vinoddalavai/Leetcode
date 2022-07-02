from typing import List


class ContainerWithMostWater:
    def max_area(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            result = max(result, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return result


heights_list = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print("Container with most water has area of : " +
      str(ContainerWithMostWater().max_area(heights_list)))
