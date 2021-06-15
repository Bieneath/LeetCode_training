# 比较好的加点法 https://leetcode.com/problems/min-cost-to-connect-all-points/discuss/843921/PythonGolang-Just-add-points-greedily
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        l = len(points)
        dist = [float('inf')] * l # dist始终存储探索过的与points[i]相连的最短边长度
        seen = {0}
        cur = ret = 0
        for _ in range(l-1): # 总共在点0的基础上还要添加l-1个点（边）
            for i, (x, y) in enumerate(points):
                if i in seen: continue
                dist[i] = min(dist[i], abs(points[i][0] - points[cur][0]) + abs(points[i][1] - points[cur][1]))
            dis, cur = min((d, i) for i, d in enumerate(dist))
            dist[cur] = float('inf') # 这步的意义是防止dist[cur]又一次作为最小值出现在dist中
            seen.add(cur)
            ret += dis
        return ret

# # 解题思路：https://leetcode-cn.com/problems/min-cost-to-connect-all-points/solution/c-kruskalprimsuan-fa-jie-da-by-yizhe-shi/
# # 加边法
# from itertools import combinations
# import heapq
# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         # 1.根据点与点的距离从小到大进行排序，这里通过heaq和combinations来实现。
#         hq = []
#         for i, j in combinations(range(len(points)), 2):
#             dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
#             heapq.heappush(hq, [dist, (i, j)])
#         # 并查集部分，作用是判断两个点是否已经属于同一组内
#         dic = {}
#         def find(x):
#             if x != dic.setdefault(x, x):
#                 dic[x] = find(dic[x])
#             return dic[x]
#         ret = 0
#         while hq:
#             d, (x, y) = heapq.heappop(hq)
#             if find(x) != find(y): # 只有当x与y不在同一组内，才将它们合并，并计算距离
#                 dic[find(y)] = find(x)
#                 ret += d
#         return ret