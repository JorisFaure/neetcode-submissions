class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = {i:[] for i in range(numCourses)}

        for courses in prerequisites :
            adjlist[courses[0]].append(courses[1])

        visited = set()

        def dfs(course) :
            if course in visited :
                return False
            if adjlist[course] == [] :
                return True
            
            visited.add(course)
            for dependance in adjlist[course] :
                if not dfs(dependance) :
                    return False
            visited.remove(course)   
            return True
        
        for course in adjlist :
            if not dfs(course) :
                return False
        return True



        