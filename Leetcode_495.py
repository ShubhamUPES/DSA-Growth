from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0

        total = 0

        for i in range(len(timeSeries) - 1):
            diff = timeSeries[i + 1] - timeSeries[i]
            total += min(duration, diff)

        total += duration  # Add full duration for the last attack
        return total
