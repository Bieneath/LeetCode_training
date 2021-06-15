from collections import defaultdict
import random
class RandomizedCollection:
    def __init__(self):
        self.d = defaultdict(set) # d作为字典用来保存不同字符所在的下标位置
        self.v = [] # 保存的数据，作为列表，可以轻松通过下标找到对应的字符

    def insert(self, val: int) -> bool:
        self.d[val].add(len(self.v)) # self.d添加新的val下标位置
        self.v.append(val)
        return len(self.d[val]) == 1 # 查看当前d[val]有几个位置，如果是1，就第一次插入
        
    def remove(self, val: int) -> bool: # 这题的难点就在如何O(1)的删除某个节点，通过用self.v最后一个元素替换val所在的元素完成删除。
        # if val not in self.d: return False # 不能这样写，defaultdict如果values()为空，也可能会留下键值！
        if not self.d[val]: return False # 只要d[val]为空，就表示val不在self.v中。
        idx = self.d[val].pop() # 从d[val]下标集合中弹出一个位置，根据集合的特性，弹出的肯定是最小值，也就是最靠前的下标位置
        pos, last = len(self.v) - 1, self.v[-1] # 获得self.v最后一个元素值以及索引
        if idx < pos: # 删除时候要分一下情况，如果idx恰巧是self.v最后一个位置的索引，那么不需要进行替换操作
            self.d[last].add(idx)
            self.v[idx] = last
        self.v.pop()
        self.d[last].discard(pos)
        return True

    def getRandom(self) -> int:
        return random.choice(self.v)