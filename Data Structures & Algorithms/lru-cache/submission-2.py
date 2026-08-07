class Node:
    def __init__(self, key: int, value: int) :
        self.key = key
        self.value = value
        self.prev = None
        self.next_ = None

class LRUCache:

    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.current_capacity = 0
        self.cache = {}
        self.lru = Node(0,0)
        self.mru = Node(0,0)
        

    def get(self, key: int) -> int:
        if key not in self.cache :
            return -1
        self.cache[key].prev.next_ = self.cache[key].next_
        self.cache[key].next_.prev = self.cache[key].prev
        self.cache[key].next_ = self.mru
        self.cache[key].prev = self.mru.prev
        self.cache[key].prev.next_ = self.cache[key]
        self.cache[key].next_.prev = self.cache[key]
        return self.cache[key].value
        

    def put(self, key: int, value: int) -> None:
        if self.current_capacity == 0 :
            self.current_capacity += 1
            newNode = Node(key, value)
            newNode.next_ = self.mru
            newNode.prev = self.lru
            self.lru.next_ = newNode
            self.mru.prev = newNode
            self.cache[key] = newNode
            return

        if key in self.cache :
            self.cache[key].value = value
            self.get(key)
        else :
            if self.current_capacity == self.max_capacity: #je dépasse
                #remove least recent key
                self.cache.pop(self.lru.next_.key)
                self.lru.next_ = self.lru.next_.next_
                self.lru.next_.prev = self.lru
            else :
                self.current_capacity += 1
            newNode = Node(key, value)
            newNode.next_ = self.mru
            newNode.prev = self.mru.prev
            newNode.prev.next_ = newNode
            newNode.next_.prev = newNode
            self.cache[key] = newNode
        return
