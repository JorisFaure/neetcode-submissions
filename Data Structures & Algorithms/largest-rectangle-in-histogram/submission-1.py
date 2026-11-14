class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1 :
            return heights[0]
        res = 0

        stack = []

        stack.append(0)

        for i, val in enumerate(heights) :
            if i == 0 :
                continue
            if not stack or heights[stack[-1]] <= heights[i] :
                stack.append(i)
                continue
            right_bound = i
            while stack and heights[stack[-1]] > heights[right_bound] :
                curr = stack.pop()
                if not stack :
                    left_bound = -1
                else :
                    left_bound = stack[-1]
                area = heights[curr] * (right_bound - left_bound - 1)
                res = max(res, area)
            stack.append(i)
        right_bound = len(heights)
        while stack :
            curr = stack.pop()
            if not stack :
                left_bound = -1
            else :
                left_bound = stack[-1]
            area = heights[curr] * (right_bound - left_bound - 1)
            res = max(res, area)
        return res
