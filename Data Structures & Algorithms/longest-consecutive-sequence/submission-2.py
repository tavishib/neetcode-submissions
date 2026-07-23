class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nmap = {}
        for n in nums:
            nmap[n] = 1
        longest = 0
        for n in nmap:
            if n-1 not in nmap:
                length = 1
                while(n+length) in nmap:
                    length += 1
                longest = max(length, longest)
        return longest