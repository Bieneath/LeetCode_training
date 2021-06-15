class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def is_similar(a, b): # 题意里已经说明a与b是异位词，因此各个字母的个数是相同的
            count = 0
            for x, y in zip(a, b):
                if x != y:
                    if count > 1: return False
                    count += 1
            return True
        f = {}
        def find(x):
            if x != f.setdefault(x, x):
                f[x] = find(f[x])
            return f[x]
        for s in strs:
            f.setdefault(s, s)
            for k in f:
                if is_similar(k, s):
                    f[find(s)] = find(k)
        return sum(x == f[x] for x in f)