from typing import List


class ProductOfArrayExceptSelf:
    def product_except_self(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums))
        prefix = 1
        for index in range(len(nums)):
            if index > 0:
                result[index] = nums[index - 1] * prefix
                prefix = result[index]

        postfix = 1
        for index in range(len(nums)-1, -1, -1):
            result[index] = result[index] * postfix
            postfix = nums[index] * postfix
        return result


nums_list = [1, 2, 3, 4]
print("Product of array except self: " +
      str(ProductOfArrayExceptSelf().product_except_self(nums_list)))
