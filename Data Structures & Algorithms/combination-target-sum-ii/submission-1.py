class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.s = {}
        self.res = []
        candidates.sort()
        
        def rec(current_sum, current_path, index) :
            print(current_path)
            if current_sum == target :
                self.res.append(current_path[:])
                return
            if index >= len(candidates) or current_sum > target :
                return
            
            current_path.append(candidates[index])
            rec(current_sum + candidates[index], current_path, index + 1)
            current_path.pop()
            while index + 1 < len(candidates) and candidates[index + 1] == candidates[index] :
                index += 1
            rec(current_sum, current_path, index + 1)
        rec(0, [], 0)    
        return self.res
        