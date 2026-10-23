class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        def createGraph() :
            graph = [[] for i in range(n)]
            for [x, y] in edges :
                graph[x].append(y)
                graph[y].append(x)
            return graph
        
        graph = createGraph()

        state = [0]*n

        res = 0

        def dfs(node, parent, graph, state) :
            state[node] = 1

            for neighbour in graph[node] :
                if state[neighbour] == 2 or neighbour == parent :
                    continue
                if state[neighbour] == 1 :
                    continue
                dfs(neighbour, node, graph, state)
            state[node] = 2
            return

        for i in range(n) :
            if state[i] == 0 :
                res+=1
                dfs(i, i, graph, state)
        
        return res

        