# 构建前缀树结构
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = defaultdict(TrieNode) # 用defaultdict可以省掉一行判断语句

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            if w not in node.children: return False
            node = node.children[w]
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for w in prefix:
            if w not in node.children: return False
            node = node.children[w]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)