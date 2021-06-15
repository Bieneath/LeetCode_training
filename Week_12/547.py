# 并查集解法
class Solution:
    def findCircleNum(self, mat: List[List[int]]) -> int:
        l = len(mat)
        dic = {}
        count = 0
        def Find(x):
            dic.setdefault(x, x)
            if dic[x] != x:
                dic[x] = Find(dic[x])
            return dic[x]
        def Union(x, y):
            dic[Find(y)] = Find(x)
        for i in range(l):
            Find(i)
            for j in range(l):
                if mat[i][j] and i != j:
                    Union(i, j)
        for i in range(l):
            if dic[i] == i:
                count += 1
        return count

# # DFS解法
# class Solution:
#     def findCircleNum(self, M: List[List[int]]) -> int:
#         l = len(M)
#         ret = 0
#         seen = set() # 每次有新的朋友加入，就记入seen(录入下标)，避免重复递归和计算ret值
#         # 深度优先搜索函数
#         def dfs(index):
#             for j, v in enumerate(M[index]): # v为True或者False
#                 if v and j not in seen: # not in seen这个条件非常重要，防止重复搜索已经搜索过的路线
#                     seen.add(j)
#                     dfs(j) 

#         # 代码主干部分是遍历0~N
#         for i in range(l):
#             if i not in seen:
#                 # 递归会将与seen中存储的所有节点都搜索到并放入seen中。所以如果出现not in seen的情况，
#                 # 那就是开启了一个新的朋友圈。
#                 ret += 1 
#                 dfs(i)
#         return ret