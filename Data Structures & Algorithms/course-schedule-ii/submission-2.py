from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indegree = [0]*numCourses
        adjList = defaultdict(list)

        for pre in prerequisites :
            adjList[pre[1]].append(pre[0])
            indegree[pre[0]]+=1

        q = deque()
        res = []
        
        for i in range(len(indegree)) :
            if indegree[i] == 0 :
                q.append(i)
        
        while len(q) > 0 :
            curr = q.popleft()
            res.append(curr)

            for child in adjList[curr] :
                indegree[child] -= 1
                if indegree[child] == 0 :
                    q.append(child)
                    
        if len(res) == numCourses :
            return res
        return []
                

        