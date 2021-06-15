# 标准的回溯递归算法
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]: return False
        def dfs(i, j, cur_word):
            if not cur_word:
                return True
            c = cur_word[0]
            if i < 0 or i >= n_rows or j < 0 or j >= n_cols or '#' == board[i][j] or board[i][j] != c:
                return False
            board[i][j] = '#'
            ret = False
            if dfs(i-1, j, cur_word[1:]) or dfs(i+1, j, cur_word[1:]) or dfs(i, j-1, cur_word[1:]) or \
                dfs(i, j+1, cur_word[1:]):
                ret = True
            board[i][j] = c
            return ret
        
        n_rows, n_cols = len(board), len(board[0])
        for i in range(n_rows):
            for j in range(n_cols):
                if dfs(i, j, word):
                    return True
        return False