class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 1 :
            return nums
        prefix = [nums[i] for i in range(len(nums))]
        postfix = [nums[i] for i in range(len(nums))]
        res = [1 for i in range(len(nums))]
        for i in range(1,len(nums)) :
            prefix[i] = prefix[i-1] * nums[i]
        
        for i in range(len(nums)-2, -1, -1) :
            postfix[i] = postfix[i+1] * nums[i]
        for i in range(len(nums)) :
            if i == 0 :
                res[i] = postfix[i+1]
            elif i == len(nums) - 1 :
                res[i] = prefix[i-1]
            else :
                res[i] = prefix[i-1] * postfix[i+1] 
        return res

        