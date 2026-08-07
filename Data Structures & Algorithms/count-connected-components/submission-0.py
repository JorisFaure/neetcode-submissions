class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adjList = [[] for _ in range(n)]

        for x, y in edges :
            adjList[x].append(y)
            adjList[y].append(x)

        visited = set()
        
        def dfs(curr, par) :
            if curr in visited :
                return
            
            visited.add(curr)

            for i in range(len(adjList[curr])) :
                if adjList[curr][i] == par :
                    continue
                dfs(adjList[curr][i], curr)
            return

            

        res = 0
        for i in range(n) :
            if not i in visited :
                dfs(i, -1)
                res+=1
        return res
