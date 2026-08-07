class Node:
    def __init__(self, val = 0, key = None) :
        self.prev = None
        self.next = None
        self.val = val
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_cap = 0
        self.key_node = {}
        self.lru = Node()
        self.mru = Node()

        self.lru.next = self.mru
        self.mru.prev = self.lru

        

    def get(self, key: int) -> int:
        if key in self.key_node :
            #On débranche 
            self.key_node[key].prev.next = self.key_node[key].next
            self.key_node[key].next.prev = self.key_node[key].prev

            #On rebranche à la fin
            self.key_node[key].prev = self.mru.prev
            self.key_node[key].next = self.mru
            self.key_node[key].prev.next = self.key_node[key]
            self.mru.prev = self.key_node[key]
            return self.key_node[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        #On créer un noeud
        if key not in self.key_node :
            newNode = Node(value, key)
            self.key_node[key] = newNode
            self.curr_cap += 1
            #On débranche le noeud finale
            if self.curr_cap > self.capacity :
                del(self.key_node[self.lru.next.key])
                self.lru.next.next.prev = self.lru
                self.lru.next = self.lru.next.next
                self.curr_cap -= 1
        else :
            #On update la value et on débranche pour update la position
            self.key_node[key].val = value
            self.key_node[key].prev.next = self.key_node[key].next
            self.key_node[key].next.prev = self.key_node[key].prev

        
        #On branche le noeud à la fin
        self.key_node[key].prev = self.mru.prev
        self.key_node[key].next = self.mru
        self.key_node[key].prev.next = self.key_node[key]
        self.mru.prev = self.key_node[key]

        
