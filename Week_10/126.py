class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList: return []
        archive = [[beginWord]]
        ret = []
        temp = []
        del_list = set()
        while archive:
            for it in archive:
                if it[-1] == endWord:
                    for it in archive:
                        if it[-1] == endWord:
                            ret.append(it)
                    break
                last_word = it[-1]
                for i in range(len(last_word)):
                    for c in range(ord('a'), ord('z') + 1):
                        new_word = last_word[:i] + chr(c) + last_word[i+1:]
                        if new_word in wordList:
                            temp.append(it + [new_word])
                            # temp.append(it.append(new_word)) # it.append()没有返回值，而且这里不能公用内存地址，要创建一个新的地址
                            del_list.add(new_word)
            archive = temp
            wordList -= del_list
            temp = []
            del_list = set()
        return ret


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