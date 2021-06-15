# 与146题相同，使用OrderedDict类实现更新顺序以及先进先出的功能
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.data = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.data: return -1
        self.data.move_to_end(key, last=True)
        return self.data[key]

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.data.move_to_end(key, last=True)
        elif len(self.data) >= self.capacity:
                self.data.popitem(last=False)
        self.data[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)