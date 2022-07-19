from typing import List
import heapq


class KthLargestElementInAnArray:
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
