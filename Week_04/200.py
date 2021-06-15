class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        n_rows, n_cols = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            if i<0 or i>n_rows-1 or j<0 or j>n_cols-1 or '0' == grid[i][j] or '#' == grid[i][j]:
                return
            grid[i][j] = '#'
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
            return

        for i in range(n_rows):
            for j in range(n_cols):
                if '1' == grid[i][j]:
                    count += 1
                    dfs(i, j)
        return count