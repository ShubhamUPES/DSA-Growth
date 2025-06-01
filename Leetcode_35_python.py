from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        found = False
        for i in range(len(nums)):
            if target == nums[i]:
                found = True
                return i  # Return index if found

        if not found:
            nums.append(target)
            nums.sort()
            return nums.index(target)  # Return index after inserting and sorting
