from typing import List, Counter
import collections
import heapq


class TaskScheduler:
    def least_interval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        q = collections.deque()
        time = 0

        while max_heap or q:
            time += 1

            if max_heap:
                temp_count = 1 + heapq.heappop(max_heap)

                if temp_count:
                    q.append([temp_count, time + n])

            if q and time == q[0][1]:
                heapq.heappush(max_heap, q.popleft()[0])

        return time
