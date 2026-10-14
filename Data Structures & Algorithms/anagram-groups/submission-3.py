class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            sorted_string = "".join(sorted(s))
            if sorted_string not in groups:
                groups[sorted_string] = []
            groups[sorted_string].append(s)
        return list(groups.values())