from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        movements = ((0,-1),(1,0),(0,1), (-1,0))

        visited = set()
            

        q = deque()
        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == 0 :
                    q.append((i,j,0))

        while len(q) > 0 :
            curr_i, curr_j, curr_dist = q.popleft()
            for x,y in movements :
                if (0<=curr_i+x<len(grid) and 0<=curr_j+y<len(grid[0])) and grid[curr_i+x][curr_j+y] != -1 and grid[curr_i+x][curr_j+y] != 0 and (curr_i+x, curr_j+y) not in visited:
                    visited.add((curr_i+x,curr_j+y))
                    grid[curr_i+x][curr_j+y] = curr_dist+1
                    q.append((curr_i+x, curr_j+y, grid[curr_i+x][curr_j+y]))
            
        
        return