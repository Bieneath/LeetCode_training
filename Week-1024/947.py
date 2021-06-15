# 此并查集解法在合并什么上有了突破；首先如果有点(x, y)，意味着所有x行以及y列上的点都能被归并，如果有点(x, z)，那么x, y, z能被归并在一起，因为此时z列上的所有点也能被归并。因此能发现我们归并的不单可以是一群点，而是一群行或列。我们可以让y归并给x！这里有个问题，就是x与y的值可能相同，为了从数值上区分行1和列1，我们将列1变成列~1
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = {}
        def find(x):
            if x != uf.setdefault(x, x):
                uf[x] = find(uf[x])
            return uf[x]
        for x, y in stones:
            uf[find(~y)] = find(x)
        count = sum(x == uf[x] for x in uf)
        return len(stones) - count

from collections import defaultdict
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows, cols = defaultdict(set), defaultdict(set)
        for i, (x, y) in enumerate(stones):
            rows[x].add(i)
            cols[y].add(i)
        tree = {}
        def find(x):
            if x != tree.setdefault(x, x):
                tree[x] = find(tree[x])
            return tree[x]
        for i, (x, y) in enumerate(stones):
            for it in rows[x]:
                tree[find(it)] = find(i)
            for it in cols[y]:
                tree[find(it)] = find(i)
        count = sum(tree[x] == x for x in tree)
        return len(stones) - count