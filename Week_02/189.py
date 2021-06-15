class Solution:
    def rotate(self, n: List[int], k: int) -> None:
        l = len(n)
        k = k % l
        def revserse(i, j):
            while i < j:
                n[i], n[j] = n[j], n[i]
                i, j = i+1, j-1
        revserse(0, l-k-1)
        revserse(l-k, l-1)
        revserse(0, l-1)