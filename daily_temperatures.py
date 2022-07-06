from typing import List


class DailyTemperatures:
    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        stack, output = [], [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp, index))
            while stack and temp > stack[-1][0]:
                removed_element = stack.pop()
                r_temp, r_index = removed_element[0], removed_element[1]
                output[r_index] = index - r_index
            stack.append((temp, index))
        return output


temps = [73, 74, 75, 71, 69, 72, 76, 73]
print(DailyTemperatures().daily_temperatures(temps))
