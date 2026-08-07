class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) < 2 :
            return [0]
        res = [0]*len(temperatures)
        stack = []
        stack.append(0)
        for i in range(1, len(temperatures)) :
            days_count = 0
            while stack and temperatures[stack[-1]] < temperatures[i] :
                colder = stack.pop()
                res[colder] = i - colder
            stack.append(i)
        return res





        