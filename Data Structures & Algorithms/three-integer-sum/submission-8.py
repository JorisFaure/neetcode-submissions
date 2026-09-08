class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        print(nums)
        
        left = 0
        res = []

        for left in range(0, len(nums) - 2) :
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            i = left + 1
            right = len(nums) - 1
            while i < right :
                total = nums[left] + nums[i] + nums[right]

                if total == 0 :
                    res.append([nums[left], nums[i], nums[right]])
                    i+=1
                    right-=1
                    while (nums[i] == nums[i-1]) and i < right :
                        i+=1
                    while (nums[right] == nums[right+1]) and i < right :
                        right-=1
                
                if total < 0 and i < right:
                    i+=1
                elif 0 < total and i < right :
                    right -= 1
        return res
