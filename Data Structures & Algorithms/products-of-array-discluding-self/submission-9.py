class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) < 2 :
            return nums
        prefix = [n for n in nums]
        suffix = [n for n in nums]

        for i in range(1, len(prefix)) :
            prefix[i] = prefix[i]*prefix[i-1]
        for i in range(len(suffix)-2, -1, -1) :
            suffix[i] = suffix[i]*suffix[i+1]
        
        nums[0] = suffix[1]
        for i in range(1, len(nums)-1) :
            nums[i] = prefix[i-1]*suffix[i+1]
        nums[len(nums)-1] = prefix[len(nums)-2]

        return nums



        
        