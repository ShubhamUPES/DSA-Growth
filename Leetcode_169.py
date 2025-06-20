class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        majority_count = len(nums) // 2

        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

            if freq[num] > majority_count:
                return num
