# 这题不要被并查集吓到，直接用暴力搜索(配合字典)也能通过！这里有个小技巧，判断是否是情侣可以用异或判断，比如2与3是情侣对，2=3^1同时3=2^1。
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        d = {v: k for k, v in enumerate(row)} # 先获得数字对应的下标字典
        count = 0
        for i in range(0, len(row), 2):
            pair = row[i]^1 # 可以使用异或的方法快速求出情侣数
            if row[i+1] == pair: continue
            pos = d[pair]
            row[i+1], row[pos] = row[pos], row[i+1]
            d[row[pos]] = pos
            # d[pair] = i+1 # pair不会再被使用，可以不用更新pair的哈希表
            count += 1
        return count