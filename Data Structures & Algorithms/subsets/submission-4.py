class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def subsets_rec(curr_subset, i) :
            if i == len(nums) :
                output.append(curr_subset[::1])
                return
            left = subsets_rec(curr_subset, i+1)
            curr_subset.append(nums[i])
            right = subsets_rec(curr_subset, i+1)
            curr_subset.pop()
        subsets_rec([], 0)
        return output

        