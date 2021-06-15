from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.dict = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.dict[c]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.dict:
                return False
            cur = cur.dict[c]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.dict:
                return False
            cur = cur.dict[c]
        return True