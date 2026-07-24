class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nmap = {} 
        for i in range(len(nums)):
            nmap[nums[i]] = i
            for j in range(i, len(nums)):
                target =  0 - nums[i] - nums[j]
                arr = sorted([target, nums[i], nums[j]])
                if target in nmap and nmap[target] != i and nmap[target] != j and arr not in ans:
                    ans.append(arr)
                nmap[nums[j]] = j
            nmap = {}
        return ans
