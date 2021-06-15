class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        # 这题和246题非常相似
        i1 = i2 = i3 = 0
        ret = [1]
        for i in range(1, k):
            n1, n2, n3 = 3*ret[i1], 5*ret[i2], 7*ret[i3]
            v = min(n1, n2, n3)
            ret.append(v)
            if v == n1:
                i1 += 1
            if v == n2:
                i2 += 1
            if v == n3:
                i3 += 1
        return ret[k-1]