class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums2 = []  # define nums2 inside the function
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums2.append(nums[i])
        for j in range(len(nums)):
            if nums[j] % 2!=0 :
                nums2.append(nums[j])
        return nums2  # return the result
