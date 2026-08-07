class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        if len(points) < 2 :
            return 0

        adjList = defaultdict(list)

        #Construct the gaph with an Adjancy list
        for i in range(len(points)):
            for j in range(len(points)):
                adjList[i].append(j)
        print(adjList)

        heap = []

        heapq.heappush(heap, (0, 0))
        visited = set()
        res = 0

        # Always choose the nearest point
        while len(visited) < len(points) :
            dist, p = heapq.heappop(heap)
            if p in visited :
                continue
            res += dist

            for child in adjList[p] :
                
                if child not in visited :
                    child_x, child_y = points[child]
                    px, py = points[p]
                    dist = abs(px - child_x) + abs(py - child_y)
                    heapq.heappush(heap, (dist, child))
            
            visited.add(p)
        
        return res


