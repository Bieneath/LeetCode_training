from collections import defaultdict
# 构建前缀树节点
class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = defaultdict(TrieNode)

# 构建前缀树方法
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ret = []
        if not words or not board: return ret
        n_rows, n_cols = len(board), len(board[0])
        # 构建遍历二维图标方法
        def dfs(i, j, node, text):
            if node.isWord:
                ret.append(text)
                node.isWord = False # 防止在ret中append重复的单词
            # 遇到i, j越界、board[i][j]为'#'（此单词已经被使用过）或者board[i][j]不在前缀树的时候直接返回
            if i < 0 or i >= n_rows or j < 0 or j >= n_cols or '#' == board[i][j] or board[i][j] not in node.children:
                return
            t = board[i][j]
            node = node.children[t]
            board[i][j] = '#' # 这里有个逻辑上的顺序，node前进到node.children[t]时候，再将board[i][j]设置为'#'比较好。
            dfs(i-1, j, node, text + t)
            dfs(i+1, j, node, text + t)
            dfs(i, j-1, node, text + t)
            dfs(i, j+1, node, text + t)
            board[i][j] = t
 
        # main function
        tree = Trie()
        root = tree.root
        # 构建前缀树
        for word in words:
            tree.insert(word)
        for i in range(n_rows):
            for j in range(n_cols):
                dfs(i, j, root, "")
        return ret