import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        graph = [[] for i in range(len(points))]

        for i in range(len(points)) :
            for j in range(i+1, len(points)) :
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]) 
                graph[i].append((dist, j))
                graph[j].append((dist, i))

        heap = []

        for i in range(len(graph[0])) :
            heapq.heappush(heap, graph[0][i])
        
        res = 0
        count_node = len(graph)
        visited = set()

        visited.add(0)


        while heap :
            #On choisis à chaque fois le voisin le plus proche, puis on empile les voisns du voisins etc..
            dist, node = heapq.heappop(heap)
            if node in visited :
                continue
            
            visited.add(node)

            res += dist
            count_node -= 1

            if count_node == 0 :
                break

            for neighbours in graph[node] :
                heapq.heappush(heap, neighbours)



        return res


        