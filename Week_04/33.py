class Solution:
    def search(self, n: List[int], target: int) -> int:
        # 二分搜索
        if not n: return -1
        l, r = 0, len(n) - 1
        while l <= r:
            mid = (l + r) // 2
            if n[mid] == target:
                return mid
            if n[0] <= n[mid]:
                if n[0] <= target < n[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if n[mid] < target <= n[len(n)-1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1