from collections import defaultdict
class TreeNode:
    def __init__(self):
        self.isWord = False
        self.dic = defaultdict(TreeNode)

class WordDictionary:
    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.dic[c]
        cur.isWord = True

    def search(self, word: str) -> bool:
        def helper(cur, i):
            if i == len(word):
                return cur.isWord
            c = word[i]
            if c is '.':
                if any(helper(cur.dic[it], i + 1) for it in cur.dic):
                    return True
                # for it in cur.dic:
                #     if helper(cur.dic[it], i+1): return True
            elif c in cur.dic:
                return helper(cur.dic[c], i+1)
            return False
        return helper(self.root, 0)