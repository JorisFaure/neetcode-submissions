from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
        queue = deque()

        fresh = 0

        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == 2 :
                    queue.append((i, j))
                elif grid[i][j] == 1 :
                    fresh += 1
        
        minute = 0
        while queue and fresh > 0:
            minute +=1 
            for i in range(len(queue)) :
                curr_i, curr_j = queue.popleft()
                for dir_i, dir_j in directions :
                    if curr_i + dir_i < 0 or len(grid) <= curr_i + dir_i or curr_j + dir_j < 0 or len(grid[0]) <= curr_j + dir_j or grid[curr_i + dir_i][curr_j + dir_j] != 1:
                        continue
                    queue.append((curr_i + dir_i, curr_j + dir_j)) 
                    grid[curr_i + dir_i][curr_j + dir_j] = 2
                    fresh -= 1
        
        
        if fresh > 0 :
            return -1
        return minute


        