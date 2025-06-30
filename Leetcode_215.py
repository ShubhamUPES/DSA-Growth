class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        c=sorted(nums)
        return c[-k]
        
