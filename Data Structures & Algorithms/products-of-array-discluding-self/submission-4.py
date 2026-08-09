class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        start = 1
        end = nums[1]

        left = [1 for elt in nums]
        right = [1 for elt in nums]

        cumul = 1

        for i in range(0, len(nums)) :
            left[i] = cumul
            cumul *= nums[i]
        
        cumul = 1

        for j in range(len(nums)-1, -1, -1) :
            right[j] = cumul
            cumul *= nums[j]

        for i in range(0, len(nums)) :
            nums[i] = left[i]*right[i]
        return nums

            
        