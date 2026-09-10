class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = nums[0]
        i = 0
        while i < len(nums)-1:
            if nums[i] > nums[i+1]:
                return nums[i+1]
            else:
                i = i + 1
                continue
        return start