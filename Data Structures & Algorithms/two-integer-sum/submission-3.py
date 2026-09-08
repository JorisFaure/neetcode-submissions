class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, n in enumerate(nums) :
            r = target - n

            if r in indices :
                return [indices[r], i]
            indices[n] = i
        return [-1, -1]



      
        