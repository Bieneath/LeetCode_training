from collections import defaultdict
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        l = len(ring)
        # 第一步，写个计算start到end下标最短距离得函数
        def min_dis(start, end):
            d = abs(end - start)
            return min(d, l - d)
        # 第二步，找出每个字母出现在哪些位置
        pos = defaultdict(set)
        for i, v in enumerate(ring):
            pos[v].add(i)
        # 第三步，用一个字典保存候选字母索引和到该字母的最短路径键对值，每次pre都只保存当前字母所有的{索引:路径数}字典
        pre = {0:0}
        for c in key:
            temp = {}
            for idx in pos[c]:
                temp[idx] = float('inf')
                for it in pre:
                    # 这里是加速点，当前字母c的某个位置需要保存的是当前最短的路径，这样可以大大减少搜索量
                    temp[idx] = min(temp[idx], min_dis(it, idx) + pre[it])
            pre = temp # 用当前字母的所有{索引:路径数}的字典代替前一个字母的{索引:路径数}字典
        return min(pre.values()) + len(key)