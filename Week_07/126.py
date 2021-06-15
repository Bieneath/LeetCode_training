# 在ret添加合法路径上处理不是很好，用字典来保存路径代码上能更精简。
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        ret = []
        wordList = set(wordList)
        if endWord not in wordList: return []
        path = [[beginWord]]
        temp = []
        del_list = set()
        while path:
            for it in path:
                if it[-1] == endWord:
                    for it in path:
                        if it[-1] == endWord:
                            ret.append(it)
                    return ret
                last = it[-1]
                for i in range(len(last)):
                    for c in range(ord('a'), ord('z')+1):
                        new_word = last[:i] + chr(c) + last[i+1:]
                        if new_word in wordList:
                            temp.append(it + [new_word])
                            del_list.add(new_word)
            path = temp
            temp = []
            wordList -= del_list
            del_list = set()
        return []


# from collections import defaultdict
# class Solution:
#     def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
#         wordList = set(wordList)
#         if endWord not in wordList: return []
#         ret = []
#         layer = {beginWord: [[beginWord]]}
#         while layer:
#             new_layer = defaultdict(list)
#             for word in layer:
#                 if word == endWord:
#                     for it in layer[word]:
#                         ret.append(it)
#                 else:
#                     for i in range(len(word)):
#                         for c in range(97, 123):
#                             new_word = word[:i] + chr(c) + word[i+1:]
#                             if new_word in wordList:
#                                 # 此处和127题不一样的地方，一定要注意，因为要返回所有的路径，如果提前把'cog'删了，
#                                 # 会导致其他的路线无法找到最后的'cog'，最后只能返回一条路径
#                                 # wordList.remove(new_word) 
#                                 new_layer[new_word].extend([it+[new_word] for it in layer[word]])
#             wordList -= set(new_layer.keys())
#             layer = new_layer
#         return ret