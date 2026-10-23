import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for i in range(n+1)]
        for (ui, vi, ti) in times :
            graph[ui].append((vi, ti))

        visit = set()
        heap = []
        heapq.heappush(heap, (0, k))

        max_time = 0

        while heap :
            (time, node) = heapq.heappop(heap)

            if node in visit :
                continue
            visit.add(node)

            max_time = max(max_time, time)
            for neighbour, dist in graph[node] :
                if neighbour in visit :
                    continue
                heapq.heappush(heap, (time + dist, neighbour))
        
        
        return max_time if len(visit) == n else -1


        