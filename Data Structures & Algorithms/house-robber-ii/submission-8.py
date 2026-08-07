class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return nums[0]

        

        def rec(arr, i) :
            if i >= len(arr) :
                return 0

            if i in self.memo :
                return self.memo[i]  
                  
            left = arr[i] + rec(arr, i+2)
            right = rec(arr, i+1)
            self.memo[i] = max(left, right)
            return self.memo[i]

        self.memo = {}
        skip_first = rec(nums[:-1], 0)
        self.memo = {}
        skip_last = rec(nums[1:], 0)

        return max(skip_first, skip_last)    

        