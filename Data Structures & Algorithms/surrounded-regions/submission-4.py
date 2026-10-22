class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = ((-1, 0), (0,1), (1, 0), (0,-1))


        def dfs(i, j) :
            # finish = True
            # #On check si on est sur une cellule final d'une zone
            # for x, y in directions: 
            #     if board[i+x][j+y] == 'O' and (not (i+x, j+y) in seen):
            #         finish = False
            #         break
            # if finish :
            #     return True
            

            board[i][j] = 'E'
            for x, y in directions:
                if 0 <= i+x < len(board) and 0 <= j+y < len(board[0]) and board[i+x][j+y] == 'O' :
                    dfs(i+x, j+y)

            return




            

        for i in range(1) :
            for j in range(len(board[0])) :
                if board[i][j] == 'O' :
                    dfs(i, j)
                if board[len(board) - 1][j] == 'O' :
                    dfs(len(board) - 1, j)
        for i in range(len(board)) :
            for j in range(1) :
                if board[i][j] == 'O' :
                    dfs(i, j)
                if board[i][len(board[0]) - 1] == 'O' :
                    dfs(i, len(board[0]) - 1)

        for i in range(len(board)) :
            for j in range(len(board[0])) :
                if board[i][j] == 'O' :
                    board[i][j] = 'X'
                elif board[i][j] == 'E' :
                    board[i][j] = 'O'
        return
    
        

        