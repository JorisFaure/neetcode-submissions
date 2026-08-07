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
            print("i: ", curr_i, " j: ", curr_j, " curr_dist: ", curr_dist)
            for x,y in movements :
                if (0<=curr_i+x<len(grid) and 0<=curr_j+y<len(grid[0])) and grid[curr_i+x][curr_j+y] != -1 and grid[curr_i+x][curr_j+y] != 0 and (curr_i+x, curr_j+y) not in visited:
                    print("i+x: ", curr_i+x, " j+y: ", curr_j+y, " curr_dist: ", curr_dist+1)
                    grid[curr_i+x][curr_j+y] = min(curr_dist+1, grid[curr_i+x][curr_j+y])
                    q.append((curr_i+x, curr_j+y, grid[curr_i+x][curr_j+y]))
            visited.add((curr_i,curr_j))
        
        return    

        [[4,-1,0,1]
        ,[3,2,1,-1]
        ,[1,-1,2,-1]
        ,[0,-1,3,4]]