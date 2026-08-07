class Solution:
    def rob(self, nums: List[int]) -> int:
        n_house = len(nums) - 1
        self.memo = {}

        def rec(current_house) :
            if current_house > n_house :
                return 0
            if current_house in self.memo :
                return self.memo[current_house]
            left = rec(current_house + 2)
            right = rec(current_house + 3)
            self.memo[current_house] = nums[current_house] + max(left, right)

            return self.memo[current_house]
            

        a = rec(0)
        b = rec(1)    
        return max(a,b)