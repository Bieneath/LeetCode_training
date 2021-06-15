class Solution:
    def fourSum(self, n: List[int], target: int) -> List[List[int]]:
        # 这题的一个解题思路就是在拿掉一个数字的情况下做三数和
        # 解题代码其实不是最有解，做了一些重复递归。
        if len(n) < 4: return []
        ret = set()
        n.sort()
        l = len(n)
        j, i = 0, 1
        for i in range(l-2):
            # if i > 1 and n[i] == n[i-1]: continue
            for j in range(i):
                if j > 0 and n[j] == n[j-1]: continue
                le, ri = i+1, l-1
                while le < ri:
                    v = n[j] + n[i] + n[le] + n[ri]
                    if v < target: le += 1
                    if v > target: ri -= 1
                    if v == target:
                        ret.add((n[j], n[i], n[le], n[ri]))
                        while le < ri and n[le] == n[le+1]: le += 1
                        le += 1
                        while le < ri and n[ri] == n[ri-1]: ri -= 1
                        ri -= 1
        return list(ret)