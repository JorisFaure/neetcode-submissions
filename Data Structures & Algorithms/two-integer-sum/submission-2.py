class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        viewed = set()
        indices = {}


        for i, n in enumerate(nums) :
            r = target - n

            if r in viewed :
                return [indices[r], i]
            indices[n] = i
            viewed.add(n)
        return [-1, -1]



      
        