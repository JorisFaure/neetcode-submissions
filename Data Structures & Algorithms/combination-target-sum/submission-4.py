class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        self.res = []

        nums.sort()


        def combi(curr, total, i) :

            if i >= len(nums) :
                return

            if total > target :
                return
            
            if total == target :
                self.res.append(curr.copy())
                return
            
            combi(curr, total, i+1)
            
            if total+nums[i] > target :
                return
            curr.append(nums[i])
            combi(curr, total+nums[i], i)
            curr.pop()

            return
        
        combi([], 0, 0)

        return self.res
            


        