class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0  # represents dp[i-1]
        prev2 = 0  # represents dp[i-2]

        for num in nums:
            temp = prev1
            prev1 = max(prev1, prev2 + num)
            prev2 = temp

        return prev1
