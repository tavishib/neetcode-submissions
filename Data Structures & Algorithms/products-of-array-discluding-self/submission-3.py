class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        num_zeros = 0
        ans = []
        for n in nums:
            if n != 0:
                product = product * n
            else:
                num_zeros = num_zeros + 1
        for i in range(len(nums)):
            if num_zeros > 1:
                ans.append(0)
            elif num_zeros == 1:
                if nums[i] == 0:
                    ans.append(product)
                else:
                    ans.append(0)
            else:
                ans.append(int(product/nums[i]))
        return ans