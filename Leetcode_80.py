class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        expected = []
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] <= 2:
                expected.append(num)

        # Copy back to nums for in-place effect
        for i in range(len(expected)):
            nums[i] = expected[i]

        return len(expected)
