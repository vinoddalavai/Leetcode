import math
from typing import List


class KokoEatingBananas:
    def min_eating_speed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right
        while left <= right:
            mid = (right + left) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            if hours <= h:
                result = min(mid, result)
                right = mid - 1
            else:
                left = mid + 1
        return result


piles1, h1 = [3, 6, 7, 11], 8
print("Koko can eat " + str(KokoEatingBananas().min_eating_speed(piles1, h1)) + " bananas per hour.")
