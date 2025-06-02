

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_set = set(nums)  # O(n) time and space
        result = []

        for i in range(1, n + 1):  # O(n)
            if i not in num_set:  # O(1) average case
                result.append(i)
        
        return result
