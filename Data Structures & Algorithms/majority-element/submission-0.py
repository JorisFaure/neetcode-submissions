class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq = {}

        res = nums[0]

        for i in range(len(nums)) :
            freq[nums[i]] = freq.get(nums[i], 0) + 1
            if freq[nums[i]] > freq[res] :
                res = nums[i]
        
        return res


        