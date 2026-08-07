class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = len(board)
        c = len(board[0])

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(r) :
            for j in range(c) :
                if board[i][j] == "." :
                    continue
                if board[i][j] in rows[i] :
                    return False
                if board[i][j] in cols[j] :
                    return False
                current_box = (i//3)*3 + j//3
                if board[i][j] in boxes[current_box] :
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                boxes[current_box].add(board[i][j])

        # for i in range(r) :
        #     col_set = set()
        #     for j in range(c) :
        #         if not board[i][j].isdigit() :
        #             continue
        #         if board[i][j] in col_set :
        #             return False
        #         col_set.add(board[i][j])
        
        # for j in range(c) :
        #     row_set = set()
        #     for i in range(r) :
        #         if not board[i][j].isdigit() :
        #             continue
        #         if board[i][j] in row_set :
        #             return False
        #         row_set.add(board[i][j])
        # boxes = defaultdict(set)
        # for i in range(r) :
        #     for j in range(c) :
        #         if not board[i][j].isdigit() :
        #             continue
        #         current_box = (i//3)*3 + (j//3)
        #         print(i,j, current_box)
        #         if board[i][j] in boxes[current_box]:
        #             return False
        #         boxes[current_box].add(board[i][j])
        return True

        