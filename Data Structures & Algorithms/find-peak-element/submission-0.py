class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2

        while left < right :

            if mid == left and nums[mid] > nums[mid+1] :
                return mid
            if mid == left and nums[mid] < nums[mid+1] :
                return mid+1
            if nums[mid-1] < nums[mid] > nums[mid+1] :
                return mid
            if nums[mid-1] > nums[mid] < nums[mid+1] or nums[mid-1] < nums[mid] < nums[mid+1] :
                left = mid+1
            elif nums[mid-1] > nums[mid] > nums[mid+1] :
                right = mid

            mid = (left + right) // 2
                
                
        return mid