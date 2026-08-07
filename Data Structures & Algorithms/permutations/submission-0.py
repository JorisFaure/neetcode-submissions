class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def rec(left_choices,curr_path) :
            if len(left_choices) == 0 :
                self.res.append(curr_path[:])
                return
            for v in list(left_choices) :
                left_choices.remove(v)
                curr_path.append(v)
                rec(left_choices, curr_path)

                curr_path.pop()
                left_choices.add(v)
        rec(set(nums), [])
        return self.res
            

        