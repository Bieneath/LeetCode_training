# # 并查集解法
# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         if not board or not board[0]: return None
#         # 首先定义并查集方法 Find, Union；Find用来寻找当前节点的根节点
#         # Union用来合并两个节点
#         dic = {} # 用来查询x的上级节点dic[x]。
#         def Find(x): # Find用来找到x的根节点
#             dic.setdefault(x, x) # x不在dic的时候，先初始化dic[x] = x
#             if x != dic[x]:
#                 dic[x] = Find(dic[x])
#             return dic[x]
#         def Union(x, y): # y并入x！y的根节点设置为x的根节点。
#             dic[Find(y)] = Find(x)
#         # 分组，边上的'O'以及与其联通的'O'以dummy为根；
#         # 内部的'O'为另外一类。
#         n_rows, n_cols = len(board), len(board[0])
#         dummy = n_rows * n_cols
#         for i in range(n_rows):
#             for j in range(n_cols):
#                 if 'O' == board[i][j]:
#                     if i == 0 or i == n_rows-1 or j == 0 or j == n_cols-1:
#                         Union(i*n_cols + j, dummy)
#                     else:
#                         for a, b in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#                             if board[i+a][j+b] == 'O':
#                                 Union(i*n_cols + j, (i+a)*n_cols + j+b)
#         # 收尾，将不与dummy一组的'O'全部改成'X'
#         for i in range(n_rows):
#             for j in range(n_cols):
#                 if 'O' == board[i][j]:
#                     if Find(dummy) != Find(i*n_cols + j):
#                         board[i][j] = 'X'
#         return

# DFS解法
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        # 递归函数
        def helper(i, j):
            if i < 0 or i > n_rows-1 or j < 0 or j > n_cols-1 or board[i][j] == 'X' or board[i][j] == '#':
                return
            # if board[i][j] == 'O'
            board[i][j] = '#' # 把'O'暂时设为'#'
            for u, v in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                helper(i + u, j + v)
        # 先搜索一圈“board”外围，遇到"O"就进入递归，把和边框相连的"O"全部暂改为"#"
        n_rows, n_cols = len(board), len(board[0])
        for i in [0, n_rows-1]:
            for j in range(n_cols):
                helper(i, j)
        for j in [0, n_cols-1]:
            for i in range(n_rows):
                helper(i, j)
        # 遍历整个“board”，将"#"从新改回"O"，"O"改为"X"
        for i in range(n_rows):
            for j in range(n_cols):
                if board[i][j] == 'O': 
                    board[i][j] = 'X'
                elif board[i][j] == '#': 
                    board[i][j] = 'O'