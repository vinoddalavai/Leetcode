from typing import List


class Search2DMatrix:
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        r_left, r_right = 0, len(matrix) - 1
        while r_left <= r_right:
            r_mid = (r_right + r_left) // 2
            row = matrix[r_mid]
            last_element = len(matrix[r_mid]) - 1
            if row[last_element] >= target >= row[0]:
                c_left, c_right = 0, last_element
                while c_left <= c_right:
                    c_mid = (c_right + c_left) // 2
                    if target == row[c_mid]:
                        return True
                    elif target > row[c_mid]:
                        c_left = c_mid + 1
                    else:
                        c_right = c_mid - 1
                return False
            elif target > row[last_element]:
                r_left = r_mid + 1
            elif target < row[0]:
                r_right = r_mid - 1
        return False


nums_matrix, target_num = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13
print("Searching for " +
      str(target_num) +
      " in the matrix: " +
      str(Search2DMatrix().search_matrix(nums_matrix, target_num)))
