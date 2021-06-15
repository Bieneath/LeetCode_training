class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return -1
        roots = {}
        def find(x):
            if x != roots.setdefault(x, x):
                roots[x] = find(roots[x])
            return roots[x]
        for x, y in connections:
            roots[find(y)] = find(x)
        # 找出有多少台PC处在离线状态
        unconnected_pc = n - len(roots)
        # 找出现有的连通图中有多少个聚落
        n_groups = sum(x == roots[x] for x in roots)
        return unconnected_pc + n_groups - 1