class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        word_map = {}
        counter = 0
        for s in strs:
            sorted_string = "".join(sorted(s))
            if sorted_string in word_map:
                ans[word_map[sorted_string]].append(s)
            else:
                word_map[sorted_string] = counter
                ans.append([s])
                counter = counter + 1
        return ans
