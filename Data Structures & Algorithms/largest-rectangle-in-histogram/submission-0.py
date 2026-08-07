class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack_index = []
        stack_height = []

        for i in range(len(heights)) :
            
            last_index = i
            while stack_height and stack_height[-1] > heights[i] :
                last_index = stack_index.pop()
                last_area = stack_height.pop() * (i - last_index)
                max_area = max(max_area, last_area)
                
            stack_height.append(heights[i])
            stack_index.append(last_index)
        
        for i in range(len(stack_height)) :
            last_index = stack_index[i]
            last_area = stack_height[i] * (len(heights) - last_index)
            max_area = max(max_area, last_area)
        return max_area