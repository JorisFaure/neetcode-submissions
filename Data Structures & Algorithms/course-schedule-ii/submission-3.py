class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        def createGraph() :
            graph = [[] for i in range (numCourses)]
            for course, pre in prerequisites :
                graph[course].append(pre)
            return graph

        def dfs(node, graph, path, state) :
            state[node] = 1
            for neighbour in graph[node] :
                if state[neighbour] == 1 :
                    return False
                if state[neighbour] == 2 :
                    continue
                if not dfs(neighbour, graph, path, state) :
                    return False
            state[node] = 2
            path.append(node)
            return True




        state = [0]*numCourses
        graph = createGraph()
        res = []
        for course in range(numCourses) :
            if state[course] == 0 :
                if not dfs(course, graph, res, state) :
                    return []
        
        return res
        