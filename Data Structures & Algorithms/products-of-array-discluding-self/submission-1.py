class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1]*l

        prefix = 1
        for i in range(1, l) :
            prefix *= nums[i-1]
            res[i] = prefix
            

        postfix = 1
        for i in range(l-2, -1, -1) :
            postfix *= nums[i+1]
            res[i] *= postfix
        return res
        


        return res

        