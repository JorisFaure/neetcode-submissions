class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        taken = [False]* len(nums)
        nums.sort()

        def rec(taken, nums, permut) :
            if len(permut) == len(nums) :
                res.append(permut.copy())
                return

            i = 0

            while i < len(nums) :
                if taken[i] :
                    i+=1
                    continue
                if not taken[i] :
                    permut.append(nums[i])
                    taken[i] = True
                    rec(taken, nums, permut)
                    permut.pop()
                    taken[i] = False
                i+=1
                while i < len(nums) and nums[i-1] == nums[i] :
                    i+=1
                
            return
        rec(taken, nums, [])
        return res
        