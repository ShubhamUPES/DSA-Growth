class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(set(nums))
        cur_len = 1
        max_len = 1
        
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i] + 1:
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                cur_len = 1
        
        return max_len
