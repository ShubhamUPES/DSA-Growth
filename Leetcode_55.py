class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        for i in range(len(nums)):
            if i > reachable:
                return False
            reachable = max(reachable, i + nums[i])
        return True


'''Another Sol
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums):
            if i + nums[i] >= len(nums) - 1:
                return True
            if nums[i] == 0:
                return False
            i += 1
        return False
'''
