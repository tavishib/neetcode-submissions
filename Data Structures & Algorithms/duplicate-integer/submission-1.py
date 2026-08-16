class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nmap = {}
        for i in range(len(nums)):
            if nums[i] in nmap:
                return True
            else:
                nmap[nums[i]] = 1
        return False
