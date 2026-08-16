class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmap = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in nmap:
                ans = [nmap[needed],i]
                return ans
            else:
                nmap[nums[i]] = i
        return [0,0]