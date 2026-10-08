class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        self.res = []

        nums.sort()


        def combi(curr, total, i) :

            if i >= len(nums):
                return
            
            if total == target :
                self.res.append(curr.copy())
                return

            for index in range(i, len(nums)) :
                if total+nums[index] > target :
                    return
                curr.append(nums[index])
                combi(curr, total+nums[index], index)
                curr.pop()
            return
        
        combi([], 0, 0)

        return self.res
            


        