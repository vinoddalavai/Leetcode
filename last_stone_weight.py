from typing import List
import heapq


class LastStoneWeight:
    def last_stone_weight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        stones.append(0)
        return abs(stones[0])


stone_weights = [2, 7, 4, 1, 8, 1]
print("Last stone remaining: ")
print(LastStoneWeight().last_stone_weight(stone_weights))
