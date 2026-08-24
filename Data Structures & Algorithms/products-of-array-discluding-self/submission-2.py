class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        hasZero = False
        hasMoreZero = False
        for n in nums:
            if n != 0:
                product = product * n
            if n == 0 and not hasZero:
                hasZero = True
            elif n == 0 and hasZero:
                hasMoreZero = True
        ans = []
        for n in nums:
            if hasMoreZero:
                ans.append(0)
            elif not hasZero:
                ans.append(int(product/n))
            elif hasZero and n != 0:
                ans.append(0)
            elif hasZero and n == 0:
                ans.append(int(product))
            else:
                ans.append(0)
        return ans