class Solution:
    def solve(self, board: List[List[str]]) -> None:
        movements = ((0,-1), (1,0), (0,1), (-1,0))
        
        
        def dfs(i,j) :
            if i == -1 or j == -1 or i == len(board) or j == len(board[0]) :
                return False
            if board[i][j] == "X" :
                return True
            
            is_surrounded = True
            visited.add((i, j))
            current_area.add((i, j))

            for x,y in movements :
                if (i+x,j+y) not in current_area :
                    is_surrounded = is_surrounded and dfs(i+x, j+y)
            return is_surrounded

        visited = set()
        for i in range(len(board)) :
            for j in range(len(board[0])) :
                if board[i][j] == "O" and (i,j) not in visited :
                    current_area = set()
                    if dfs(i,j) :
                        for x,y in current_area :
                            board[x][y] = "X"
        return 


