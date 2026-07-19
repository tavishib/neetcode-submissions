class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        ans = sorted(freq, key = freq.get, reverse = True)
        return ans[:k]