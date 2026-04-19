class MinStack:

    def __init__(self):
        self.stack = []      # Main stack
        self.min_stack = []  # Min tracker

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack: 
            self.min_stack.append(val)
        elif val <= self.min_stack[-1]:
            self.min_stack.append(val)


    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
