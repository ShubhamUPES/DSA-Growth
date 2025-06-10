class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        result = True
        for i in range(len(nums) - 1):
            if (nums[i] % 2 == nums[i + 1] % 2):
                result = False
                break
        return result
