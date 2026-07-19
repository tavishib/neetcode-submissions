class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmap = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in nmap:
                return [nmap[needed], i]
            nmap[nums[i]] = i