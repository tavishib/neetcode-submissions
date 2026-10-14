class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nmap = {}
        for n in nums:
            if n in nmap:
                return True
            else:
                nmap[n] = 1
        return False