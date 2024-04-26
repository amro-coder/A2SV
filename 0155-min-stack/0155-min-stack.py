class MinStack:

    def __init__(self):
        self.stack=[]
        self.stackMin=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stackMin or val<=self.stackMin[-1]:
            self.stackMin.append(val)

    def pop(self) -> None:
        if self.stackMin and self.stackMin[-1]==self.stack.pop():
            self.stackMin.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackMin[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()