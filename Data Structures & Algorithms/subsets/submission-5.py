class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        self.res = []

        def subset(nums, curr, start) :
            if start >= len(nums) :
                self.res.append(curr.copy())
                return
            subset(nums, curr, start+1)
            curr.append(nums[start])
            subset(nums, curr, start+1)
            curr.pop()
            return

        subset(nums, [], 0)

        return self.res





        