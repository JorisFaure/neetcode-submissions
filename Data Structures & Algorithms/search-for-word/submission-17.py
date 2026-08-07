class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        len_y = len(board)
        len_x = len(board[0])
        l_w = len(word)
        self.movements = ((-1, 0), (0, 1), (1,0), (0,-1))

        def backtrack(i, j, w_index, visited) :
            if board[i][j] != word[w_index] :
                return False
            if w_index == l_w-1 :
                return True

            res = False
            visited[i][j] = 1
            for x,y in self.movements :
                if (0<=i+y<len(board)) and (0<=j+x<len(board[0])) and not visited[i+y][j+x] :
                     if backtrack(i+y, j+x, w_index+1, visited) :
                        res = True
                        break
            visited[i][j] = 0
                
            return res
            



        for i in range(len_y) :
            for j in range(len_x) :
                visited = [[0 for x in range(len_x)] for y in range(len_y)]
                flag = backtrack(i, j, 0, visited)
                if flag :
                    return True
        return False


        


        