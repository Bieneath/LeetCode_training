from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList) # 这步很关键，后面会大量用到查找，set的查找效率远超list！
        dq = deque([[beginWord, 1]])
        while dq:
            word, dis = dq.popleft()
            if word == endWord: return dis
            for i in range(len(word)):
                for c in range(97, 123): # 小写字母ASCII码为97到122
                    new_word = word[:i] + chr(c) + word[i+1:]
                    if new_word in wordList:
                        wordList.remove(new_word)
                        dq.append([new_word, dis+1])
        return 0

# 双向探索算法，比上面一种算法要快
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList) # 这步很关键，后面会大量用到查找，set的查找效率远超list！
        if endWord not in wordList: return 0
        wordList1 = wordList.copy() # 从beginWord开始探索和从endWord开始探索各自需要一份独立的字典
        wordList2 = wordList.copy()
        wordList2.remove(endWord) # 在从后往前的字典中删除endword，这样首尾就对称了
        # 探索新的单词函数
        def find_new_word(words, w_list):
            temp = set()
            for word in words:
                for i in range(wl):
                    for c in range(97, 123):
                        new_word = word[:i] + chr(c) + word[i+1:]
                        if new_word in w_list:
                            w_list.remove(new_word) # 从wordList中删除已经探索的单词。
                            temp.add(new_word)
            return temp, w_list

        wl = len(beginWord)
        from_start = set([beginWord])
        from_end = set([endWord])
        count = r_count = 1
        flag = 1 # 使用flag作为交互探索的指示标记
        while from_start and from_end: # from_start或from_end出现空时候，说明路线断了，直接返回0就可以了
            if from_start & from_end:
                return count + r_count - 1
            if flag:
                from_start, wordList1 = find_new_word(from_start, wordList1)
                count += 1
            else:
                from_end, wordList2 = find_new_word(from_end, wordList2)
                r_count += 1
            flag = flag^1 # ^异或，1^1 = 0, 0^1 = 1
        return 0