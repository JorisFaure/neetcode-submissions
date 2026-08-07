class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start = 0
        end = 0
        n = len(nums)
        max_ = float('-inf')
        curr_total = 0
        while start < n and end < n:
            curr_total += nums[end]
            max_ = max(curr_total, max_)
            if curr_total < 0 :
                curr_total = 0
                start = end + 1
                end = start
                continue
            end+=1
        for i in range(start, end) :
            curr_total -= nums[i]
            max_ = max(curr_total, max_)
        return max_
        