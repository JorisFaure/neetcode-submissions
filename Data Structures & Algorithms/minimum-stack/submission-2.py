class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = []
        

    def push(self, val: int) -> None:
        if not self.minVal :
            self.minVal.append(val)
        else :
            self.minVal.append(min(val, self.minVal[-1]))
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minVal.pop()
        

    def top(self) -> int:
        return self.stack[-1]

        

    def getMin(self) -> int:
        return self.minVal[-1]
        
