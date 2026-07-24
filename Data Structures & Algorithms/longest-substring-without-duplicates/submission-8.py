class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        longest = 0
        cmap = {}
        for i in range(len(s)):
            if s[i] in cmap and cmap[s[i]] >= start:
                start = cmap[s[i]]+1
            cmap[s[i]] = i
            longest = max(longest, i-start+1)
        return longest