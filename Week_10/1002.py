# 精通Counter方法的基础上再熟练应用reduce和map方法
from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        return reduce(Counter.__and__, map(Counter, A)).elements()

# 灵活使用Counter方法
from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        dic = Counter(A[0])
        for w in A:
            dic &= Counter(w)
        return dic.elements()

# 最low的代码
from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A: return []
        dic = Counter(A[0])
        for i, w in enumerate(A):
            if 0 == i:
                continue
            temp = Counter(w)
            inter_key = set(tuple(dic.keys())) & set(tuple(temp.keys()))
            new_dic = {}
            for k in inter_key:
                new_dic[k] = min(dic[k], temp[k])
            dic = new_dic
        ret = []
        for i in dic:
            for j in range(dic[i]):
                ret.append(i)
        return ret