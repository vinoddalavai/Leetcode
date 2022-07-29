import heapq
from collections import defaultdict
from typing import List


class NetworkDelayTime:
    def network_delay_time(self, times: List[List[int]], n: int, k: int):
        adj_list = defaultdict(list)
        for src, dest, time in times:
            adj_list[src].append((dest, time))
        min_heap = [(0, k)]
        heapq.heapify(min_heap)
        visited = set()
        time = 0
        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in visited:
                continue
            visited.add(n1)
            time = max(time, w1)
            for n2, w2 in adj_list[n1]:
                if n2 not in visited:
                    heapq.heappush(min_heap, (w1 + w2, n2))
        return time if len(visited) == n else -1