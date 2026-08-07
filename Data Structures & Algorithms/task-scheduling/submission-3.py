from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if len(tasks) == 0 :
            return 0
        
        max_heap = []
        self.freq_map = {}
        for t in tasks :
            self.freq_map[t] = self.freq_map.get(t, 0) + 1
        for t in self.freq_map.keys() :
            heapq.heappush(max_heap, -self.freq_map[t])
        time = 0
        q = deque()
        
        while len(max_heap) > 0 or len(q) > 0 :
            time+=1
            if len(max_heap) > 0:
                count = heapq.heappop(max_heap)+1
                if count < 0 :
                    q.append([count, time + n])
            if q and q[0][1] == time :
                elt = q.popleft()
                heapq.heappush(max_heap, elt[0])
        return time
