from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        adjList = defaultdict(list)

        for pre in prerequisites :
            indegree[pre[1]]+=1
            adjList[pre[0]].append(pre[1])

        #Je prend ceux qui ont un indegree de 0 et je les met dans une queue
        queue = deque()
        for i in range(len(indegree)) :
            if indegree[i] == 0 :
                queue.append(i)
        
        while len(queue) > 0 :
            curr = queue.popleft()
            for node in adjList[curr] :
                indegree[node]-=1
                if indegree[node] == 0 :
                    queue.append(node)
        
        for i in range(len(indegree)) :
            if indegree[i] != 0 :
                return False
        return True
        #Je dépile une fois et j'enleve le indegree des enfants de ce noeud
        #Je rempile ceux qui ont un indegree de 0
        #Je repete tant que la pile n'est pas nul
        #Si après la pile j'ai encore un indegree > 0, alors il y a un cycle et je return False.
        #Sinon, je return True
             
            
            


            
        