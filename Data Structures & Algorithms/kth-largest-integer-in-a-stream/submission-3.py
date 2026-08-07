import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.curr_space = 0
        self.heap = []
        for elt in nums :
            heapq.heappush(self.heap, elt)
            self.curr_space += 1
            if self.curr_space > self.k :
                heapq.heappop(self.heap)
                self.curr_space -=1
            


        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        self.curr_space += 1
        if self.curr_space > self.k :
            heapq.heappop(self.heap)
        return self.heap[0]
        
