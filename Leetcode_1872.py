class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:

        n = len(stones)

        # Step 1: Calculate prefix sums
        prefix = [0] * n
        prefix[0] = stones[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]

        # Step 2: Start DP from the end
        dp = prefix[-1]

        # Step 3: Go backwards
        for i in range(n - 2, 0, -1):
            dp = max(dp, prefix[i] - dp)

        return dp
