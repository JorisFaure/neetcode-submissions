from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        queue = deque()
        seen = set()


        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == 0 :
                    queue.append((i, j))
                    seen.add((i, j))


        dist = 0
        while queue :
            for i in range(len(queue)) :
                (i, j) = queue.popleft()
                grid[i][j] = dist
                for (x, y) in directions : 
                    if (i+x, j+y) in seen or i+x < 0 or i+x >= len(grid) or j+y < 0 or j+y >= len(grid[0]) or grid[i+x][j+y] == -1 :
                        continue
                    queue.append((i+x, j+y))
                    seen.add((i+x, j+y))
            dist+=1
        return
        