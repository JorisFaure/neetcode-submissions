class Solution:
    output = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
        def subsets_rec(curr_subset, i) :
            if i == len(nums) :
                self.output.append(curr_subset[::1])
                return
            left = subsets_rec(curr_subset, i+1)
            curr_subset.append(nums[i])
            right = subsets_rec(curr_subset, i+1)
            curr_subset.pop()
        subsets_rec([], 0)
        return self.output

        