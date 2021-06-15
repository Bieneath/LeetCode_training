class Solution:
    def threeSum(self, n: List[int]) -> List[List[int]]:
        ret = []
        n.sort()
        l = len(n)
        for k in range(l - 2):
            if k > 0 and n[k] == n[k-1]: continue
            i, j = k+1, l-1
            while i < j:
                v = n[k] + n[i] + n[j]
                if v == 0:
                    ret.append([n[k], n[i], n[j]])
                    while i < j and n[i+1] == n[i]: i += 1
                    i += 1
                    while i < j and n[j-1] == n[j]: j -= 1
                    j -= 1
                elif v < 0:
                    i += 1
                elif v > 0:
                    j -= 1
        return ret