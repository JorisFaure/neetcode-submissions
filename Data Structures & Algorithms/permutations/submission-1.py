class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def dfs(curr, chosen) :

            if len(curr) == len(nums) :
                self.res.append(curr.copy())
                return
            
            for j in range(0, len(nums)) :
                if chosen[j] :
                    continue
                curr.append(nums[j])
                chosen[j] = True
                dfs(curr, chosen)
                curr.pop()
                chosen[j] = False
            return

        chosen = [0 for i in range(len(nums))]
        dfs([], chosen)

        return self.res
        