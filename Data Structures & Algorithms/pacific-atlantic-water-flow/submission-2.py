class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = ((-1, 0), (0,1), (1, 0), (0, -1))

        atlantic = set()
        pacific = set()

        def dfs(i, j, ocean) :
            if ocean == "atlantic" :
                atlantic.add((i, j))
            elif ocean == "pacific" :
                pacific.add((i,j))
            
            for x, y in directions :
                if 0 <= i+x < len(heights) and 0 <= j+y < len(heights[0]) and heights[i+x][j+y] >=  heights[i][j]:
                    if ocean == "atlantic" and (i+x, j+y) not in atlantic :
                        dfs(i + x, j + y, ocean)
                    elif ocean == "pacific" and (i+x, j+y) not in pacific :
                        dfs(i + x, j + y, ocean)
            return
        
        for i in range(1) :
            for j in range(len(heights[0])) :
                dfs(i, j, "pacific")
                dfs(len(heights) - 1, j, "atlantic")
        for i in range(len(heights)) :
            for j in range(1) :
                dfs(i, j, "pacific")
                dfs(i, len(heights[0]) - 1, "atlantic")

        res = []
        
        for i in range(len(heights)) :
            for j in range (len(heights[0])) :
                if (i, j) in atlantic and (i, j) in pacific :
                    res.append([i, j])

        return res



        