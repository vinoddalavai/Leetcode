from typing import List
import heapq


class KthLargestElementInAStream:
    def __init__(self, k: int, nums: List[int]) -> None:
        self.min_heap, self.k = nums, k
        heapq.heapify(self.min_heap)

        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]


if __name__ == "__main__":
    obj = KthLargestElementInAStream(3, [4, 5, 8, 2])
    print(obj.add(3))
    print(obj.add(5))
    print(obj.add(10))
    print(obj.add(9))
    print(obj.add(4))
