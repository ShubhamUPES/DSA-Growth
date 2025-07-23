class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        reachable = 0
        curr_end = 0

        for i in range(n - 1):
            reachable = max(reachable, i + nums[i])
            if i == curr_end:
                jumps += 1
                curr_end = reachable

        return jumps
