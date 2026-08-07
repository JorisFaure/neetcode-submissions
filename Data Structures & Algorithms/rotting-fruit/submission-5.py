from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()
        visited = set()

        movements = ((0,-1), (1,0), (0,1), (-1,0))

        nb_fresh = 0

        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == 2 :
                    q.append((i,j))
                elif grid[i][j] == 1 :
                    nb_fresh+=1
        
        if len(q) == 0 and nb_fresh == 0 :
            return 0
        
        
        minute = -1

        while len(q) > 0 :
            minute+=1
            for i in range(len(q)) :
                i,j = q.popleft()

                for x,y in movements :
                    if (0 <= x+i < len(grid) and 0 <= y+j < len(grid[0])) and ((i+x, j+y) not in visited) :
                        if grid[i+x][j+y] == 1 :
                            visited.add((i+x, j+y))
                            grid[i+x][j+y] = -1
                            q.append((i+x, j+y))
            

        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == 1 :
                    return -1
        
        return minute


        