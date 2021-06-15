import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ret = []
        board = ["." * n for _ in range(n)]
        check_row = [1] * n
        check_col = [1] * n
        check_p45 = [1] * (2*n-1)
        check_n45 = [1] * (2*n-1)
        # 递归函数
        def dfs(i):
            if i == n: # 递归终止条件
                # 当列表是多维时，最好用copy.deepcopy()进行复制，防止出现意想不到的情况;虽然这题用board.copy()也不会错，因为board中存放的是str，str类型的内存地址只有一个。
                ret.append(copy.deepcopy(board))
                return
            for j in range(n):
                if check_row[i] and check_col[j] and check_p45[i+j] and check_n45[n-1+j-i]:
                    board[i] = board[i][:j] + "Q" + board[i][j+1:]
                    check_row[i], check_col[j], check_p45[i+j], check_n45[n-1+j-i] = [0] * 4
                    dfs(i+1)
                    board[i] = board[i][:j] + "." + board[i][j+1:]
                    check_row[i], check_col[j], check_p45[i+j], check_n45[n-1+j-i] = [1] * 4
        # 执行递归
        dfs(0)
        return ret