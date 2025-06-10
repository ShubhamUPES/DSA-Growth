class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        b = sorted(nums)
        for i in range(0, len(b), 2):
            if b[i] != b[i+1]:
                return False
        return True
