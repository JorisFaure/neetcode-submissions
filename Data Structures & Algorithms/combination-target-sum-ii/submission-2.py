class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        self.res = []

        def dfs(i, curr, total) :
            if total == target :
                self.res.append(curr.copy())
                return
            if i >= len(candidates) or total > target :
                return

            j = i
            while j < len(candidates) :
                if total + candidates[j] > target :
                    return
                curr.append(candidates[j])
                dfs(j+1, curr, total+candidates[j])
                curr.pop()
                while j+1 < len(candidates) and candidates[j] == candidates[j+1] :
                    j+=1
                j+=1  
            return
        
        dfs(0, [], 0)

        return self.res