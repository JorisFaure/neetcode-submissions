class LinkedList:
    
    def __init__(self):
        self.linked_list = []
        self.size = 0

    
    def get(self, index: int) -> int:
        if (self.size <= index) :
            return -1
        return self.linked_list[index]
        

    def insertHead(self, val: int) -> None:
        new_head = [val]
        self.linked_list = new_head + self.linked_list
        self.size += 1
        

    def insertTail(self, val: int) -> None:
        self.linked_list = self.linked_list + [val]
        self.size += 1
        

    def remove(self, index: int) -> bool:
        if (self.size <= index) :
            return False
        new_list = []
        for i, elt in enumerate(self.linked_list) :
            if (i == index) :
                continue
            new_list += [elt]
        self.linked_list = new_list
        self.size -= 1
        return True
        

    def getValues(self) -> List[int]:
        return self.linked_list
        
