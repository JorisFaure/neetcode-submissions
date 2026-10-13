class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        res = nums[0]
        curr = 0


        for end in range(len(nums)) :
            if curr < 0 :
                curr = 0
            curr+=nums[end]
            res = max(res, curr)

        return res

        