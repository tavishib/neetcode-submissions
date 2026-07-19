class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n_map = {}
        for i in range(len(nums)):
            if nums[i] in n_map:
                return True
            n_map[nums[i]] = i
        return False