# 如下方法的改进版本，思路一致，只是建立一个字典，key是结尾的单词，value是当前所有以key作为结尾单词的path集合 https://leetcode.com/problems/word-ladder-ii/discuss/40482/Python-simple-BFS-layer-by-layer
from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        wordList -= set(beginWord)
        if endWord not in wordList: return []
        layer = defaultdict(list)
        layer[beginWord] = [[beginWord]]
        alpahbet = list(map(chr, range(97, 97+26)))
        l = len(endWord)
        while layer:
            next_layer = defaultdict(list)
            for word in layer:
                if word == endWord:
                    return layer[word]
                for i in range(l):
                    for c in alpahbet:
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in wordList:
                            next_layer[next_word] += [it + [next_word] for it in layer[word]]
            layer = next_layer
            wordList -= set(next_layer.keys())
        return []

# from collections import deque
# class Solution:
#     def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
#         wordList = set(wordList)
#         if endWord not in wordList: return []
#         ret, dq = [], deque([[beginWord]])
#         l = len(beginWord)
#         valid_words = set()
#         alphabet = list(map(chr, range(97, 97+26)))
#         while dq:
#             sz = len(dq)
#             for _ in range(sz):
#                 path = dq.popleft()
#                 word = path[-1]
#                 if word == endWord:
#                     ret.append(path)
#                     continue # 如果发现有一个path的末尾为endWord，就不停continue直到抽干dq
#                 for i in range(l):
#                     letter = word[i]
#                     for c in alphabet:
#                         if letter == c: continue
#                         next_word = word[:i] + c + word[i+1:]
#                         if next_word in wordList:
#                             valid_words.add(next_word)
#                             dq.append(path + [next_word])
#             wordList -= valid_words # 从字典中去除已近被使用过的单词，防止走重复路线
#             valid_words = set()
#         return ret