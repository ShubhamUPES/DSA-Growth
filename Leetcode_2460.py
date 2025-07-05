class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # Step 1: Apply the doubling rule
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0

        # Step 2: Move all zeros to the end
        nums = [x for x in nums if x != 0] + [0] * nums.count(0)
        return nums
