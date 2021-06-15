from collections import defaultdict
class Solution
    def groupAnagrams(self, strs List[str]) - List[List[str]]
        dd = defaultdict(list)
        # 构建一个字典，用来一次性将异位词归类，字典key要能区分不同的异位词种类
        for word in strs
            key = [0]  26
            for c in word
                key[ord(c) - 97] += 1 # ord('a') == 97
            dd[tuple(key)].append(word) # list, set, dict不能做字典的key!
        return list(dd.values())