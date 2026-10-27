class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        i = 0
        left = 1
        right = len(nums)-1

        nums.sort()

        while i < len(nums)-2 :
            while left < right :
                if i > 0 and nums[i] == nums[i-1] :
                    i+=1
                    left = i+1
                    continue

                s = nums[i] + nums[left] + nums[right]
                if s == 0 :
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    right -=1
                    while left < right and nums[right] == nums[right+1] :
                        right-=1
                elif s < 0 :
                    left += 1
                elif s > 0 :
                    right -= 1
            i+=1
            left = i+1
            right = len(nums)-1
        return res

                
                
            

        