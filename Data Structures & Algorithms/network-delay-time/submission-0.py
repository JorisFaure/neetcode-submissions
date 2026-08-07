import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = [0]*n
        distance_from_k = [float('inf')]*n
        previous = {i:-1 for i in range(1, n+1)}
        neighbours = {i:[] for i in range(1, n+1)}
        for (ui, vi, ti) in times :
            neighbours[ui].append((vi, ti))
        print(visited)
        print(distance_from_k)
        print(previous)
        print(neighbours)

        distance_from_k[k - 1] = 0
        priority = []
        heapq.heappush(priority, (0,k))

        while len(priority) > 0 :
            (_,to_visit) = heapq.heappop(priority)
            visited[to_visit - 1] = 1

            for (neighbor, dist) in neighbours[to_visit] :
                if visited[neighbor - 1] == 1 :
                    continue
                new_distance = distance_from_k[to_visit - 1] + dist
                if new_distance < distance_from_k[neighbor - 1] :
                    distance_from_k[neighbor - 1] = new_distance
                    previous[neighbor] = to_visit
                    heapq.heappush(priority, (distance_from_k[neighbor - 1], neighbor))
        if min(visited) == 0 :
            return -1
        return max(distance_from_k)


