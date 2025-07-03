class Solution:
    def binarysearch(self, arr, k):
        for i in range(len(arr)):
            if arr[i] == k:
                return i
        return -1


#binary search
class Solution:
    def binarysearch(self, arr, k):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == k:
                return mid
            elif arr[mid] < k:
                low = mid + 1
            else:
                high = mid - 1
        return -1
