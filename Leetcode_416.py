class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        possible = set([0])
        
        for num in nums:
            new_sums = set()
            for s in possible:
                if s + num == target:
                    return True
                if s + num < target:
                    new_sums.add(s + num)
            possible.update(new_sums)
        
        return target in possible
