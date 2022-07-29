from collections import defaultdict
from typing import List


class CourseSchedule:
    def can_finish(self, num_courses: int, pre_requisites: List[List[int]]) -> bool:
        pre_map = {index: [] for index in range(num_courses)}
        visited = set()
        for course, pre in pre_requisites:
            pre_map[course].append(pre)

        def dfs(c: int):
            if not pre_map[c]:
                return True
            if c in visited:
                return False
            visited.add(c)
            for p in pre_map[c]:
                if not dfs(p):
                    return False
            visited.remove(c)
            pre_map[c] = []
            return True

        for course in range(num_courses):
            if not dfs(course):
                return False
        return True
    