class MinStack:
    def __init__(self):
        self.data = []
    def push(self, x: int) -> None:
        # data中存放一对值，第一个是x，第二个是当前为止的最小值
        cur_min = self.getMin()
        if cur_min is None or cur_min > x:
            cur_min = x
        self.data.append([x, cur_min])
    def pop(self) -> None:
        self.data.pop()
    def top(self) -> int:
        return self.data[-1][0]
    def getMin(self) -> int:
        if not self.data:
            return None
        return self.data[-1][1]