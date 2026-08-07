from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if not times :
            return -1
        
        graph = defaultdict(list)

        for ui, vi, ti in times :
            graph[ui].append((vi, ti))
        
        visited = set()

        heap = []
        heapq.heappush(heap, (0, k))
        res = 0

        while heap : 
            curr_weight, node = heapq.heappop(heap)

            if node in visited :
                continue
            
            res = max(res, curr_weight)

            for child, w in graph[node] :
                if node not in visited :
                    heapq.heappush(heap, (w + curr_weight, child))
            
            visited.add(node)
        if len(visited) == n :
            return res
        return -1
            

        

            
        

        

        