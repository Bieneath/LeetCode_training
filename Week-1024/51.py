# 51题,bitmask+递归；这题用python有个隐藏的难点，关于列表的值传递问题，复合列表中，每个元素保存的是一个子列表的地址。
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ret = []
        check_col = [1] * n
        check_45, check_135 = [[1]*(2*n-1) for _ in range(2)]
        board = ['.' * n for _ in range(n)]
        def helper(i, board):
            if i == n:
                ret.append(board) # 其实这个board保存的是一组列表地址的列表
            for j in range(n):
                if check_col[j] and check_45[i+j] and check_135[n-1-i+j]:
                    check_col[j] = check_45[i+j] = check_135[n-1-i+j] = 0
                    temp_board = board.copy()
                    temp_board[i] = temp_board[i][:j] + 'Q' + temp_board[i][j+1:]
                    helper(i + 1, temp_board)
                    check_col[j] = check_45[i+j] = check_135[n-1-i+j] = 1
        helper(0, board)
        return ret