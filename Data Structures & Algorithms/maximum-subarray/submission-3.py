class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums :
            return 0

        res = 0

        acc = 0
        res = float('-inf')


        for i, n in enumerate(nums) :
            if acc > nums[i] or (acc > 0 and nums[i] > 0):
                acc+= nums[i]
            else :
                acc = nums[i]
            res = max(res, acc)
        return res        