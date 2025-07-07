from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bed = [0] + flowerbed + [0]  # Step 1: Pad with 0s
        count = 0
        i = 0

        while i < len(bed):
            if bed[i] == 0:
                zero_count = 0
                while i < len(bed) and bed[i] == 0:
                    zero_count += 1
                    i += 1
                # Step 2: For a gap of k zeros, (k - 1) // 2 flowers can be planted
                count += (zero_count - 1) // 2
            else:
                i += 1

        return count >= n
