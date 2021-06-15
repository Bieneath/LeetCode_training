# 精妙的DFS算法
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        n_rows, n_cols = len(grid), len(grid[0])
        def dfs(i, j):
            if 0 <= i < n_rows and 0 <= j < n_cols and '1' == grid[i][j]:
                grid[i][j] = '0'
                list(map(dfs, (i-1, i+1, i, i), (j, j, j-1, j+1))) # python3中map返回的是个迭代器，内部函数并未运行。使用list()使函数被运行
                return 1
            return 0
        return sum(dfs(i, j) for i in range(n_rows) for j in range(n_cols)) # for...for...这个嵌套循环中，第一个for在第二个for的外层。

# # 并查集方法（不推荐）
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid or not grid[0]: return 0
#         n_rows, n_cols = len(grid), len(grid[0])
#         dic = {}
#         def Find(x):
#             dic.setdefault(x, x)
#             if dic[x] != x:
#                 dic[x] = Find(dic[x])
#             return dic[x]
#         def Union(x, y):
#             dic[Find(y)] = Find(x)
#         def dfs(i, j, val):
#             if i < 0 or i >= n_rows or j < 0 or j >= n_cols or '0' == grid[i][j]:
#                 return
#             grid[i][j] = '0'
#             Union(val, i*n_rows + j)
#             for u, v in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#                 dfs(i+u, j+v, val)
        
#         ADD = 0
#         for i in range(n_rows):
#             for j in range(n_cols):
#                 if '0' == grid[i][j]: 
#                     continue
#                 val = n_rows * n_cols + ADD
#                 if Find(i*n_cols + j) != Find(val):
#                     dfs(i, j, val)
#                     ADD += 1
#         return ADD
            
# # DFS方法
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid or not grid[0]: return 0
#         n_rows, n_cols = len(grid), len(grid[0])
#         count = 0
#         def dfs(i, j):
#             if i < 0 or i >= n_rows or j < 0 or j >= n_cols or '0' == grid[i][j]:
#                 return
#             grid[i][j] = '0'
#             for u, v in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#                 dfs(i+u, j+v)
        
#         for i in range(n_rows):
#             for j in range(n_cols):
#                 if '1' == grid[i][j]:
#                     count += 1
#                     dfs(i, j)
#         return count