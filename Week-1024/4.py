# 二分算法
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = sorted([nums1, nums2], key=len)
        L = len(a) + len(b)
        odd = L & 1
        le, ri = 0, len(a)
        while le <= ri:
            a_ri = (le + ri) >> 1
            b_ri = ((L + 1) >> 1) - a_ri
            max_a_left = a[a_ri-1] if a_ri else -math.inf
            min_a_right = a[a_ri] if a_ri<len(a) else math.inf
            max_b_left = b[b_ri-1] if b_ri else -math.inf
            min_b_right = b[b_ri] if b_ri<len(b) else math.inf
            if max_a_left <= min_b_right and max_b_left <= min_a_right:
                if odd:
                    return float(max(max_a_left, max_b_left))
                else:
                    return (max(max_a_left, max_b_left) + min(min_a_right, min_b_right)) / 2.0
            if max_a_left > min_b_right:
                ri = a_ri - 1
            else:
                le = a_ri + 1

# # 基础的合并排序求中位数（不推荐）
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         l = len(nums1) + len(nums2)
#         mid = l >> 1
#         flag = l & 1
#         p1 = p2 = 0
#         pre = cur = None
#         for _ in range(mid + 1):
#             if p1 == len(nums1):
#                 pre, cur = cur, nums2[p2]
#                 p2 += 1
#                 continue
#             elif p2 == len(nums2):
#                 pre, cur = cur, nums1[p1]
#                 p1 += 1
#                 continue
#             if nums1[p1] < nums2[p2]:
#                 pre, cur = cur, nums1[p1]
#                 p1 += 1
#             else:
#                 pre, cur = cur, nums2[p2]
#                 p2 += 1
#         return cur if flag else (pre + cur) / 2.0