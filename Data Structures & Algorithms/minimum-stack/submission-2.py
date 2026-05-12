class MinStack:

    def __init__(self):
        self.stk1=deque()
        self.stk2=deque()
        

    def push(self, val: int) -> None:
        if not self.stk1:
            self.stk1.append(val)
            self.stk2.append(val)
        else:
            self.stk2.append(min(self.stk2[-1],val))
            self.stk1.append(val)

        

    def pop(self) -> None:
        self.stk1.pop()
        self.stk2.pop()
        

    def top(self) -> int:
        return self.stk1[-1]
        

    def getMin(self) -> int:
        return self.stk2[-1]
        
