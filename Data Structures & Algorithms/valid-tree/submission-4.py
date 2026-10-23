class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def createGraph() :
            graph = [[] for i in range (n)]
            for [x, y] in edges :
                graph[x].append(y)
                graph[y].append(x)
            return graph

        graph = createGraph()
        print(graph)
        state = [0]*n


        def dfs(node, parent, graph) :
            state[node] = 1

            for neighbour in graph[node] :
                if state[neighbour] == 2 or neighbour == parent:
                    continue
                if state[neighbour] == 1:
                    return False
                if not dfs(neighbour, node, graph) :
                    return False
            state[node] = 2
            return True

        for i in range(n) :
            if state[i] == 0 :
                if not dfs(i, i, graph) :
                    return False
                else :
                    break
        for i in range(n) :
            if state[i] == 0 :
                return False
        return True
        