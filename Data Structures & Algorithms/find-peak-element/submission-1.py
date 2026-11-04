class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2

        while left < right :
            if nums[mid] < nums[mid+1] :
                left = mid + 1
            else :
                right = mid
            mid = (left + right) // 2
                
                
        return mid