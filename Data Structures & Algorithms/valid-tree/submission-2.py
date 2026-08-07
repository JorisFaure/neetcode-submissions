class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = [[] for i in range(n)]
        for a,b in edges :
            adjList[a].append(b)
            adjList[b].append(a)

        self.edges_n = 0
        visited = set()
        self.n_edges = 0
        def dfs(node, parent) :
            if not adjList[node] :
                return True
            if node in visited :
                return False
            visited.add(node)
            for adj in adjList[node] :
                if adj == parent :
                    continue
                self.n_edges+=1
                if not dfs(adj, node) :
                    return False
    
            return True
        flag = dfs(0, -1)
        if not flag or self.n_edges != n-1 :
            return False
        return True

        