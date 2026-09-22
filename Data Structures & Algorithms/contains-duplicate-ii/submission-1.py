class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        histo = {}

        if len(nums) == 1 :
            return False
        

        histo[nums[0]] = 0
        for right in range(1, len(nums)) :
            if nums[right] in histo :
                if abs(histo[nums[right]] - right) <= k :
                    return True
            histo[nums[right]] = right
        return False
            

        