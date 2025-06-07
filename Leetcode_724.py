correct code:
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            if left_sum == total_sum - left_sum - num:
                return i
            left_sum += num

        return -1









'''class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            left_sum = 0
            right_sum = 0

            for j in range(0, i):
                left_sum += nums[j]

            for k in range(i + 1, n):
                right_sum += nums[k]

            if left_sum == right_sum:
                return i
        return -1''' #timelimit exceed
