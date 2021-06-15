# 基本的并查集方法 https://leetcode-cn.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/solution/python3-kruskalbing-cha-ji-by-smiletm-jt9y/
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # 基本的并查集函数
        def find(x, f):
            if x != f.setdefault(x, x):
                f[x] = find(f[x], f)
            return f[x]
        def get_weights(cur_weight=0, f={}, idx=None):
            for x, y, w, i in edges:
                if i == idx: continue # 设置一个idx参数，遍历到i==idx就跳过
                if find(x, f) != find(y, f):
                    cur_weight += w
                    f[find(y, f)] = find(x, f)
            return cur_weight
        # 计算出最小生成树的权重大小
        edges = [v + [i] for i, v in enumerate(edges)]
        edges = sorted(edges, key=lambda x:x[2]) # 根据权重从小到大排列
        min_weight = get_weights()
        # 遍历所有边，判断1.是否是关键边，2.是否是真·关键边
        real_key = []
        fake_key = []
        # 遍历每条边，根据weights判断是否是关键边
        for x, y, w, i in edges:
            cur_weight = get_weights(cur_weight=w, f={x:x, y:x})
            if cur_weight != min_weight: continue # 不是关键边直接跳过
            # 通过计算除i外剩余节点的最小weights判断当前的i是否是真·关键边
            cur_weight = get_weights(cur_weight=0, f={}, idx=i)
            if cur_weight == min_weight:
                fake_key.append(i)
            else: # 这里少了真·关键边，总体权重可能增加也可能减少！
                real_key.append(i)
        return [real_key, fake_key]