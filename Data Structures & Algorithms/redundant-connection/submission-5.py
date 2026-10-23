class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        

        def createGraph() :
            graph = [[] for i in range(len(edges) + 1)]

            for [x,y] in edges :
                graph[x].append(y)
                graph[y].append(x)
            
            return graph
        
        state = [0]*(len(edges)+1)

        self.cycle = set()
        self.cycle_start = -1
        def dfs(node, parent, graph, state) :
            state[node] = 1

            for neighbour in graph[node] :
                if state[neighbour] == 2 or neighbour == parent :
                    continue
                if state[neighbour] == 1 :
                    self.cycle_start = neighbour
                    self.cycle.add((node, neighbour))
                    return
                dfs(neighbour, node, graph, state)
                if self.cycle_start > 0 and self.cycle_start != node :
                    self.cycle.add((node, neighbour))
                    return
                elif self.cycle_start > 0 :
                    self.cycle.add((node, neighbour))
                    self.cycle_start = -1
                    return
            state[node] = 2
            return


        graph = createGraph()
        dfs(1, 1, graph, state)

        for i in range(len(edges)-1, -1, -1) :
            [x,y] = edges[i]

            if (x,y) in self.cycle or (y,x) in self.cycle :
                return [x,y]
        

        
        