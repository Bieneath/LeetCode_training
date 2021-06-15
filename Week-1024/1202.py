from collections import defaultdict
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        root, dic = {}, defaultdict(list)
        # 使用并查集将pairs中的关联下标合并起来
        def find(x):
            if x != root.setdefault(x, x):
                root[x] = find(root[x])
            return root[x]
        for x, y in pairs:
            root[find(y)] = find(x)
        # 使用每个下标i的根节点作为key，将s[i]插入dic中
        for i, v in enumerate(s):
            dic[find(i)].append(v)
        # 技巧点，对dic中的所有values()排序，反向的目的是为了每次pop值都是最小值
        for it in dic.values():
            it.sort(reverse=True)
        ret = ''
        for i, v in enumerate(s):
            ret += dic[find(i)].pop()
        return ret