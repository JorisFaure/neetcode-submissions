class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack_index = []
        stack_temp = []

        for i, t in enumerate(temperatures) :
            if i == 0 :
                stack_index.append(i)
                stack_temp.append(t)
            else :
                while stack_temp and stack_temp[-1] < t :
                    l_i = stack_index.pop()
                    stack_temp.pop()
                    res[l_i] = i - l_i
                stack_temp.append(t)
                stack_index.append(i)
        return res
        