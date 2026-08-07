class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        movements = [(0,-1),(1,0),(0,1),(-1,0)] #left, down, right, up
        r = len(board)
        c = len(board[0])
        for i in range(r) :
            col_set = set()
            for j in range(c) :
                if not board[i][j].isdigit() :
                    continue
                if board[i][j] in col_set :
                    return False
                col_set.add(board[i][j])
        
        for j in range(c) :
            row_set = set()
            for i in range(r) :
                if not board[i][j].isdigit() :
                    continue
                if board[i][j] in row_set :
                    return False
                row_set.add(board[i][j])
        boxes = defaultdict(set)
        for i in range(r) :
            for j in range(c) :
                if not board[i][j].isdigit() :
                    continue
                current_box = (i//3)*3 + (j//3)
                print(i,j, current_box)
                if board[i][j] in boxes[current_box]:
                    return False
                boxes[current_box].add(board[i][j])
        return True

        