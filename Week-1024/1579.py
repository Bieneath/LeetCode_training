class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        A, B = {}, {}
        def find(x, dic):
            if x != dic.setdefault(x, x):
                dic[x] = find(dic[x], dic)
            return dic[x]
        # 先对类型3的线进行合并，这点很重要！
        edges = sorted(edges, key=lambda x:x[0], reverse=True)
        count = ea = eb = 0 # 使用ea和eb记录Alice和Bob的连接线数量，如果最后ea==eb==n-1表示能实现连通
        for z, x, y in edges:
            if 1 == z:
                if find(x, A) == find(y, A): count += 1
                else: 
                    A[find(x, A)] = find(y, A)
                    ea += 1
            elif 2 == z:
                if find(x, B) == find(y, B): count += 1
                else: 
                    B[find(x, B)] = find(y, B)
                    eb += 1
            else:
                if find(x, A) == find(y, A) and find(x, B) == find(y, B):
                    count += 1
                else:
                    A[find(x, A)] = find(y, A)
                    B[find(x, B)] = find(y, B)
                    ea += 1; eb += 1
        return count if ea == eb == n-1 else -1