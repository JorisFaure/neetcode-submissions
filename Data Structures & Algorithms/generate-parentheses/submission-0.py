class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #Si j'atteint k, je dépile tout et c'est fini
        #Si la pile est vide et que j'ai pas atteint k,
        #j'empile une fois forcément
        self.res = []
        def rec(count_open, count_close, current_path) :
            if count_open == n and count_open == count_close :
                self.res.append(current_path)
                return
            if count_open < n :
                rec(count_open + 1, count_close, current_path + "(")
            if count_close < n and count_close < count_open:
                rec(count_open, count_close + 1, current_path + ")")
            return
        rec(0, 0, "")
        return self.res

            #Si count_ouv == count_f 
            #J'ajoute a mon outpur finale le current_output
