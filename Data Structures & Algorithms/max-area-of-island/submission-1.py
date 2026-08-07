class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        movements = ((0,-1), (1,0), (0,1), (-1, 0))

        def explore(i, j) :
            if grid[i][j] != 1 :
                grid[i][j] = -1
                return 0
            area_size = 1
            for x,y in movements :
                if (0<=(i+x)<len(grid)) and (0<=(j+y)<len(grid[0])):
                    grid[i][j] = -1
                    area_size += explore(i+x, j+y)
            return area_size



        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == 1 :
                    max_area = max(max_area,explore(i,j))
                grid[i][j] = -1

        return max_area
        