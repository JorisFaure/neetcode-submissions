class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suffix = [1]*n
        prefix = [1]*n

        cumul = 1

        for i in range(n) :
            prefix[i] = cumul
            cumul *= nums[i]

        cumul = 1

        for i in range(n-1, -1, -1) :
            suffix[i] = cumul
            cumul *= nums[i]
        
        for i in range(n) :
            nums[i] = prefix[i] * suffix[i]

        return nums

            
        