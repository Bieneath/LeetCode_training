class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board or not board[0]: return board
        n_row, n_col = len(board), len(board[0])
        # 递归函数
        def helper(row, col):
            mine = 0
            stack = []
            for i in [row-1, row, row+1]:
                for j in [col-1, col, col+1]:
                    if i == row and j == col: continue
                    if i < 0 or i >= n_row or j < 0 or j >= n_col: continue
                    if board[i][j] == 'M': mine += 1
                    if board[i][j] == 'E': stack.append([i, j])
            if mine == 0: 
                board[row][col] = 'B'
                while stack:
                    i, j = stack.pop()
                    helper(i, j)
            else: 
                board[row][col] = str(mine)
            return
        # 主函数
        i, j = click
        if board[i][j] == 'M': 
            board[i][j] = 'X'
            return board
        helper(i, j)
        return board