class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        w_map = {}
        ans = []
        index = 0
        for s in strs:
            sort = "".join(sorted(s))
            if sort in w_map:
                ans[w_map[sort]].append(s)
            else:
                ans.append([s])
                w_map[sort] = index
                index += 1
        return ans