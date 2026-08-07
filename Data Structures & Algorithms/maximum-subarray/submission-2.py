class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = nums[0]
        max_curr = 0

        for n in nums :
            max_curr += n
            max_ = max(max_curr, max_)
            if max_curr < 0 :
                max_curr = 0
        return max_        

        