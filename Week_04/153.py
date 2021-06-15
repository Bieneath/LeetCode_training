class Solution:
    def findMin(self, n: List[int]) -> int:
        l, r = 0, len(n) - 1
        while l <= r:
            if n[l] < n[r]: # 如果当前n[l:r+1]这段列表为正常的升序列表，那么最小值肯定就是n[l]
                return n[l]
            if l == r: # 找到了最小值
                return n[l]
            mid = (l + r) // 2
            if n[0] <= n[mid]:
                l = mid + 1
            else:
                r = mid
        return 0