from itertools import product
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        n_rows, n_cols = len(grid), len(grid[0])
        def dfs(i, j):
            if i < 0 or i >= n_rows or j < 0 or j >= n_cols or not grid[i][j]:
                return 0
            area = 1
            grid[i][j] = 0
            for u, v in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                area += dfs(i + u, j + v)
            return area
        ret = 0
        for i, j in product(range(n_rows), range(n_cols)):
            if grid[i][j]:
                ret = max(ret,  dfs(i, j))
        return ret