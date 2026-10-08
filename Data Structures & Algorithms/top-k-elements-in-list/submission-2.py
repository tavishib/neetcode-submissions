class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nmap = {}
        ans = []
        for n in nums:
            if n in nmap:
                nmap[n] = nmap[n] + 1
            else:
                nmap[n] = 1
        ordered_list = sorted(nmap.items(), key=lambda item: item[1], reverse = True)
        for i in range(k):
            ans.append(ordered_list[i][0])
        return ans