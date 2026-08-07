from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific_q = deque()
        atlantic_q = deque()

        reach_atlantic = set()
        reach_pacific = set()

        for j in range(len(heights[0])) :
            pacific_q.append((0,j))
            reach_pacific.add((0, j))
        for i in range(len(heights)) :
            pacific_q.append((i, 0))
            reach_pacific.add((i, 0))
        
        for j in range(len(heights[0])) :
            atlantic_q.append((len(heights)-1,j))
            reach_atlantic.add((len(heights)-1,j))
        for i in range(len(heights)) :
            atlantic_q.append((i, len(heights[0])-1))
            reach_atlantic.add((i, len(heights[0])-1))

        
        
        movements = ((0,-1), (1,0), (0,1), (-1,0))


        while len(pacific_q) > 0 :
            i, j = pacific_q.popleft()

            for x,y in movements :
                if (0 <= i+x < len(heights) and 0 <= j+y < len(heights[0])) and (i+x,j+y) not in reach_pacific :
                    if heights[i][j] <= heights[i+x][j+y] :
                        reach_pacific.add((i+x, j+y))
                        pacific_q.append((i+x, j+y))
        
        while len(atlantic_q) > 0 :
            i, j = atlantic_q.popleft()

            for x,y in movements :
                if (0 <= i+x < len(heights) and 0 <= j+y < len(heights[0])) and (i+x,j+y) not in reach_atlantic :
                    if heights[i][j] <= heights[i+x][j+y] :
                        reach_atlantic.add((i+x, j+y))
                        atlantic_q.append((i+x, j+y))
        res = []

        print(reach_atlantic)

        for elt in reach_atlantic :
            if elt in reach_pacific :
                x,y = elt
                res.append([x,y])
        return res


        


        