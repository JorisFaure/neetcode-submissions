class MinStack:

    def __init__(self):
        self.min_val = []
        self.stack = []
        

    def push(self, val: int) -> None:
        if len(self.min_val) > 0 :
            self.min_val.append(min(self.min_val[-1], val))
        else :
            self.min_val.append(val)
        self.stack.append(val)
        

    def pop(self) -> None:
        self.min_val.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val[-1]
