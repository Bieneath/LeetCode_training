from itertools import product
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not any(board): return []
        m, n = len(board), len(board[0])
        def dfs(i, j):
            mine = 0
            stack = []
            for u, v in product(range(-1, 2), range(-1, 2)):
                if u == v == 0: continue
                if 0 <= i+u < m and 0 <= j+v < n:
                    if 'M' == board[i+u][j+v]: mine += 1
                    if 'E' == board[i+u][j+v]: stack.append((i+u, j+v)) # 这里我经常写错，把i+u, j+v写成了i, j
            if mine > 0:
                board[i][j] = str(mine)
            else:
                board[i][j] = 'B'
                while stack:
                    dfs(*stack.pop())
        # 执行段
        i, j = click
        if board[i][j] == 'M':
            board[i][j] = 'X'
        else:
            dfs(i, j)
        return board

# from itertools import product
# class Solution:
#     def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
#         if not any(board): return []
#         m, n = len(board), len(board[0])
#         def have_mine(i, j): # 检查周围有多少地雷
#             mine = 0
#             for u, v in product(range(-1, 2), range(-1, 2)):
#                 if 0 <= i+u < m and 0 <= j+v < n and 'M' == board[i+u][j+v]:
#                     mine += 1
#             return str(mine) if mine else 'B'
#         def dfs(i, j):
#             if not (0 <= i < m and 0 <= j < n) or board[i][j] != 'E':
#                 return
#             board[i][j] = have_mine(i, j)
#             if 'B' == board[i][j]: # 根据题意，只有当board[i][j]翻完是'B'才探索周围
#                 for u, v in product(range(-1, 2), range(-1, 2)): # 这里有个点要注意，这里dfs探索的是周围8个方向
#                     dfs(i+u, j+v)
#         # 执行段
#         i, j = click
#         if board[i][j] == 'M':
#             board[i][j] = 'X'
#         else:
#             dfs(i, j)
#         return board