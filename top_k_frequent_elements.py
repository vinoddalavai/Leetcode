from typing import List


class TopKFrequentElements:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        freq_map = {i: [] for i in range(len(nums), -1, -1)}
        result = []
        for num in nums:
            count_map[num] = 1 + count_map.get(num, 0)
        for number, count in count_map.items():
            freq_map[count].append(number)
        for count, numbers in freq_map.items():
            for number in numbers:
                result.append(number)
                if len(result) == k:
                    return result
        return result


nums_list, target = [1, 1, 1, 2, 2, 3], 2
print("Top " + str(target) + " frequent numbers: \n" +
      str(TopKFrequentElements().top_k_frequent(nums_list, target)))
