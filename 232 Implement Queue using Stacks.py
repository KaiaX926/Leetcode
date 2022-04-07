class MyQueue:

    def __init__(self):
        self.res = []

    def push(self, x: int) -> None:
        return self.res.append(x)
        
    def pop(self) -> int:
        a = self.res[0]
        self.res = self.res[1:]
        return a
        

    def peek(self) -> int:
        return self.res[0]

    def empty(self) -> bool:
        return len(self.res) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
