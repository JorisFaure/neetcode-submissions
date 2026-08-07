class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []

        def rec(current_sum, current_path, current_index) :
            if current_index >= len(nums):
                return
            if current_sum > target :
                return
            if current_sum == target :
                self.res.append(current_path[:])
                return
            current_path.append(nums[current_index])
            rec(current_sum + nums[current_index], current_path, current_index)
            current_path.pop()
            rec(current_sum, current_path, current_index+1)
           
        rec(0, [], 0)
        return self.res