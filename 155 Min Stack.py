class MinStack:

    def __init__(self):
        self.new = []
    # 'High' if x > 10 else 'Low'

    def push(self, val: int) -> None:
        return self.new.append(val)

    def pop(self) -> None:
        temp = self.new[:-1] if self.new else None
        self.new = self.new[:-1]
        return temp

    def top(self) -> int:
        return self.new[-1] if self.new else None
        
    def getMin(self) -> int:
        return min(self.new) if self.new else None
        
