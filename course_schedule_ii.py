from typing import List

# TOPOLOGICAL SORT
class CourseScheduleII:
    def find_order(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = {course: [] for course in range(num_courses)}
        visited, cycle = set(), set()
        output = []
        for course, prerequisite in prerequisites:
            pre_map[course].append(prerequisite)

        def dfs(crs: int):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True

        for course in range(num_courses):
            if not dfs(course):
                return []
        return output
