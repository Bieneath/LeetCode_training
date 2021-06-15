class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ret = [1]
        i2, i3, i5 = 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = ret[i2]*2, ret[i3]*3, ret[i5]*5
            v = min(n2, n3, n5)
            ret.append(v)
            # 下面三个分支不能用if...elif...elif，因为n2,n3,n5中可能有多个等于v！
            if v == n2:
                i2 += 1
            if v == n3:
                i3 += 1
            if v == n5:
                i5 += 1
        return ret[-1]