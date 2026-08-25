class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nmap = {}
        for i in range(len(numbers)):
            needed = target - numbers[i]
            if needed in nmap:
                ans = [nmap[needed], i+1]
                return ans
            elif numbers[i] not in nmap:
                nmap[numbers[i]] = i+1
        return [0,0]