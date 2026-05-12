class MinStack:

    def __init__(self):
        self.stack=deque()
        self.stackMin=deque()
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stackMin or self.stackMin[-1]>=val:
            self.stackMin.append(val)
        

    def pop(self) -> None:
        val=self.stack.pop()
        if self.stackMin[-1]==val:
            self.stackMin.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:

        return self.stackMin[-1]

        
