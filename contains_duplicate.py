from typing import List


class ContainsDuplicate:
    def contains_duplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)
        return False


numbers1 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
numbers2 = [1, 2, 3, 4]
print(ContainsDuplicate().contains_duplicate(numbers1))
print(ContainsDuplicate().contains_duplicate(numbers2))
