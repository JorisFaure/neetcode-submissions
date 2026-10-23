class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def createGraph(numCourses) :
            hist = {}

            for i in range(numCourses) :
                hist[i] = []

            for course, pre in prerequisites :
                hist[course].append(pre)
            return hist

        def dfs(node) :
            self.state[node] = 1

            for neighbours in self.graph[node] :
                if self.state[neighbours] == 1 :
                    return False
                if self.state[neighbours] == 2 :
                    continue
                if not dfs(neighbours) :
                    return False
            self.state[node] = 2
            return True
            
        
        self.graph = createGraph(numCourses)        
        
        self.state = [0]*numCourses

        for course in range(numCourses) :
            if self.state[course] == 0 :
                if not dfs(course) :
                    return False
        return True



        