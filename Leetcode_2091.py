class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        
        a = min(min_idx, max_idx)
        b = max(min_idx, max_idx)
        
        delete_from_front = b + 1
        delete_from_back = n - a
        delete_from_both = (a + 1) + (n - b)
        
        return min(delete_from_front, delete_from_back, delete_from_both)
