from itertools import product
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        n_rows, n_cols = len(grid), len(grid[0])
        def dfs(i, j):
            if i < 0 or i >= n_rows or j < 0 or j >= n_cols or not grid[i][j]:
                return 1
            if -1 == grid[i][j]:
                return 0
            c = 0
            grid[i][j] = -1
            for u, v in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                c += dfs(i + u, j + v)
            return c
        for i, j in product(range(n_rows), range(n_cols)):
            if 1 == grid[i][j]:
                return dfs(i, j)