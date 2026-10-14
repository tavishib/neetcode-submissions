class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nmap = {}
        for n in nums:
            if n in nmap:
                nmap[n] = nmap[n] + 1
            else:
                nmap[n] = 1
        ans_list = list(sorted(nmap, key=lambda k: nmap[k], reverse=True))
        return ans_list[:k]