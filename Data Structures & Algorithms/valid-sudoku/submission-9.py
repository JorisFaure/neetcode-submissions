class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #verify rows
        for i in range(9) :
            row_numbers = set()
            for j in range(9) :
                if board[i][j].isdigit() :
                    if board[i][j] in row_numbers :
                        return False
                    row_numbers.add(board[i][j])
        #verify cols
        for i in range(9) :
            col_numbers = set()
            for j in range(9) :
                if board[j][i].isdigit() :
                    if board[j][i] in col_numbers :
                        return False
                    col_numbers.add(board[j][i])
        
        for count in range(9) :
            square_numbers = set()
            for i in range(3) :
                for j in range(3) :
                    if board[i + (3*(count//3))][j + (3*(count%3))].isdigit() :
                        if board[i + (3*(count//3))][j + (3*(count%3))] in square_numbers :
                            return False
                        square_numbers.add(board[i + (3*(count//3))][j + (3*(count%3))])
            print(square_numbers, count)
        
        return True


