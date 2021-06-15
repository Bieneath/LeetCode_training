# class Solution:
#     def merge(self, n1: List[int], l1: int, n2: List[int], l2: int) -> None:
#         minlen = min(l1, l2)
#         rest = n2[minlen: l2] if l1<l2 else n1[minlen: l1]
#         pool = []
#         for i in range(minlen):
#             pool.append(n1[i])
#             pool.append(n2[i])
#         for it in rest: pool.append(it)
#         pool.sort()
#         for i in range(len(pool)):
#             n1[i] = pool[i]

# 这题因为n1中后面有多出来的空间，所以要从大到小，从后往前搜索！
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while m>0 and n>0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n>0: # 当nums2前几位数均小于nums1的情况下:
            nums1[:n] = nums2[:n]