class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = left + (right - left) // 2
        while left != mid :
            if nums[mid] > nums[right] : # half right will be unsorted
                left = mid
            else :
                right = mid
            mid = left + (right - left) // 2
        return min(nums[mid], nums[right], nums[left])

            
        