from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.idx = None
        self.dic = defaultdict(TrieNode)
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def _insert(self, i, w):
        cur = self.root
        for c in w:
            cur = cur.dic[c]
        cur.idx = i
    def _search(self, w):
        cur = self.root
        ret = []
        for c in w:
            if c not in cur.dic: return ret
            if cur.dic[c].idx is not None:
                ret.append(cur.dic[c].idx)
            cur = cur.dic[c]
        return ret
class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        l = len(smalls)
        ret = [[] for _ in range(l)] # 这里不能使用[[]]*l的初始化方式！
        tree = Trie()
        # 将smalls插入前缀树
        for i, s in enumerate(smalls):
            tree._insert(i, s)
        # 遍历big字符串
        for i in range(len(big)):
            idxs = tree._search(big[i:])
            for idx in idxs:
                ret[idx].append(i)
        return ret