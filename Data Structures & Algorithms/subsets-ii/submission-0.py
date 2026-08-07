class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()
        def backtrack(current_path, current_index) :
            if current_index >= len(nums) :
                self.res.append(current_path[:])
                return
            current_path.append(nums[current_index])
            backtrack(current_path, current_index+1)
            current_path.pop()
            while current_index < len(nums) - 1 and nums[current_index] == nums[current_index+1] :
                current_index+=1
            backtrack(current_path, current_index+1)
            return
        backtrack([], 0)
        return self.res