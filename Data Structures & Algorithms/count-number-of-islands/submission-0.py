class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        movements = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        total_group = 0
        n_row = len(grid)
        n_col = len(grid[0])
        
        def dfs(row, cell) :
            if row < 0 or row >= n_row or cell < 0 or cell >= n_col :
                return
            if grid[row][cell] == "0" :
                return
            grid[row][cell] = "0"
            for (r, c) in movements :
                dfs(row + r, cell + c)
            return

        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == "1" :
                    total_group += 1
                    dfs(i, j)
        return total_group


        