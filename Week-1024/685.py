# 并查集方法
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        dic = {}
        par = {} # 比如a -> b，则记录par[b] = a
        record = None
        cycle = None
        def find(x):
            if x != dic.setdefault(x, x):
                dic[x] = find(dic[x])
            return dic[x]
        def union(a, b): # a -> b
            dic[find(a)] = find(b)
        for a, b in edges:
            if b in par: # 说明b的入度不为1
                record = [b, par[b], a] # record记录3三项：入度不为1的节点b，前一个相关节点par[b]和当前的相关节点a
                continue # 不连接a与b
            if find(a) == find(b): # 此时表示a，b在一个根上，如果再让union(a,b)，就形成了环
                cycle = [a, b]
            par[b] = a # 记录b的父节点是a
            union(a, b)
        if not record: # 如果没有入度超过1的节点，直接返回edges中最后的环边
            return cycle
        if cycle: # 如果有入度为2的节点，而且出现了环，那么入度为2的点和其第一个父节点形成的边就是多余边
            return [record[1], record[0]]
        else: # 如果有入度为2的节点，但是并没有环，那么入度为2的点和其第二个父节点形成的边就是多余边
            return [record[2], record[0]]