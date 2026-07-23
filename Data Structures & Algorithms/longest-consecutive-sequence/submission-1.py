class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        print(nums)
        max_len = 0
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                count += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                if count > max_len:
                    max_len = count
                count = 1
        if(len(nums) == 0):
            return 0
        return max(max_len, count)