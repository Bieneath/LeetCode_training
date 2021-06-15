from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.dict = defaultdict(TrieNode)

class TrieTree():
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        cur = self.root
        for c in word:
            cur = cur.dict[c]
        cur.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not words or not board or not board[0]: return []
        ret = []
        n_rows, n_cols = len(board), len(board[0])
        def dfs(i, j, node, path):
            if node.isEnd:
                ret.append(path)
                node.isEnd = False # 不同的路线，但是组成的单词可能相同，如果不改成False，可能会出现重复的结果
            # 筛选一下board[i][j]是否合法
            if i < 0 or i >= n_rows or j < 0 or j >= n_cols or '#' == board[i][j] or board[i][j] not in node.dict:
                return
            c = board[i][j]
            board[i][j] = '#'
            node = node.dict[c]
            dfs(i-1, j, node, path + c)
            dfs(i+1, j, node, path + c)
            dfs(i, j-1, node, path + c)
            dfs(i, j+1, node, path + c)
            board[i][j] = c
            
        # main function
        tree = TrieTree() # 实例化前缀树
        for w in words:
            tree.insert(w)
        for i in range(n_rows):
            for j in range(n_cols):
                if board[i][j] not in tree.root.dict: continue
                dfs(i, j, tree.root, "")
        return ret