from typing import List


class Permutations:
    def permute(self, nums:  List[int]) -> List[List[int]]:
        result = []

        if len(nums) == 1:
            return [nums.copy()]

        for _ in range(len(nums)):
            popped = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(popped)
            result.extend(perms)
            nums.append(popped)

        return result


if __name__ == '__main__':
    permutation = Permutations()
    input_list = [1, 2, 3]
    print("All permutations of " + str(input_list) + ":")
    print("\t" + str(permutation.permute(input_list)))
