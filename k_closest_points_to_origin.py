from typing import List
from collections import defaultdict
import heapq


class KClosestPointsToOrigin:
    def k_closest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mapping = defaultdict(list)
        result = []

        for x, y in points:
            sq_dist = x*x + y*y
            mapping[sq_dist].append([x, y])
        min_heap = list(mapping.keys())
        heapq.heapify(min_heap)
        distances = heapq.nsmallest(k, min_heap)

        for distance in distances:
            for dist in mapping[distance]:
                result.append([dist[0], dist[1]])

                if len(result) == k:
                    return result

        return result


points_list, num = [[3, 3], [5, -1], [-2, 4]], 2
print("Closest points to origin: ")
print("\t"+str(KClosestPointsToOrigin().k_closest(points_list, num)))
