class Solution:
    def totalNQueens(self, n: int) -> int:
        global count
        count = 0
        check_row = [1] * n
        check_col = [1] * n
        check_45 = [1] * (2*n - 1)
        check_135 = [1] * (2*n - 1)
        def dfs(i):
            global count
            if i == n:
                count += 1
                return
            for j in range(n):
                if check_row[i] and check_col[j] and check_45[i+j] and check_135[n+j-i-1]:
                    check_row[i], check_col[j], check_45[i+j], check_135[n+j-i-1] = [0] * 4
                    dfs(i+1)
                    check_row[i], check_col[j], check_45[i+j], check_135[n+j-i-1] = [1] * 4
        dfs(0)
        return count