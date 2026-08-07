class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        
        for i in range(len(nums) - 2) :
            if nums[i] > 0 :
                break
            if i > 0 and nums[i] == nums[i-1] :
                continue
            left = i+1
            right = len(nums) - 1
            while left < right :
                res = nums[i] + nums[left] + nums[right]
                if res == 0 :
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -=1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    continue
                if res < 0 :
                    left += 1
                if res > 0 :
                    right -= 1
            
            
        return results
            
