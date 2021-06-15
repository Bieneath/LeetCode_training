from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.data = OrderedDict()
        self.limit = capacity

    def get(self, key: int) -> int:
        if key not in self.data: return -1
        self.data.move_to_end(key=key, last=True)
        return self.data[key]

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.data.move_to_end(key=key, last=True)
        self.data[key] = value
        if len(self.data) > self.limit:
            self.data.popitem(last=False) # 弹出最先入栈的元素