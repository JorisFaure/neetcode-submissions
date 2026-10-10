import heapq
import queue
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for t in tasks :
            freq[t] = freq.get(t, 0) + 1
        
        h = []
        for keys in freq :
            heapq.heappush(h, -freq[keys])

        res = 0
        wait = deque()
        time = 0

        while len(h) > 0 or wait:
            time += 1 
            if h :
                frq = heapq.heappop(h)
                if frq != -1 :
                    wait.append((frq+1, time + n))
            
            if wait and wait[0][1] == time :
                frq, _ = wait.popleft()
                heapq.heappush(h, frq)

        
        return time
        