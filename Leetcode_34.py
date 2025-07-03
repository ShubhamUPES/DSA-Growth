class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = []
        for i in range(len(nums)):
            if nums[i] == target:
                a.append(i)
        return [a[0], a[-1]] if a else [-1, -1]

'''binary search
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft():
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return l

        def findRight():
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] <= target:
                    l = m + 1
                else:
                    r = m - 1
            return r

        left, right = findLeft(), findRight()
        if left <= right:
            return [left, right]
        return [-1, -1]
'''
