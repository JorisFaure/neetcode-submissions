from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        movements = ((0,-1),(1,0),(0,1), (-1,0))

        def bfs(i,j) :
            visited = set()
            q = deque()

            q.append((i,j, 0))

            #je dois garder en mémoire ceux que j'ai visiter dans le bfs pour pas retomber dessus

            while q :
                curr_i, curr_j, curr_dist = q.popleft()

                for x,y in movements :
                    if (0<=curr_i+x<len(grid) and 0<=curr_j+y<len(grid[0])) and grid[curr_i+x][curr_j+y] != -1 and grid[curr_i+x][curr_j+y] != 0 and (curr_i+x, curr_j+y) not in visited:
                        
                        grid[curr_i+x][curr_j+y] = min(curr_dist+1, grid[curr_i+x][curr_j+y])

                        q.append((curr_i+x, curr_j+y, grid[curr_i+x][curr_j+y]))

                visited.add((curr_i, curr_j))
            


        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == 0 :
                    bfs(i,j)

        
        return

        