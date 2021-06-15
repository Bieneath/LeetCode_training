# 思路见官方题解，建议在纸上打下草稿
# 方法三：通用双指针；因为1肯定在0后面，所以当p0、p1重合，交换过来0的时候，p0和p1都要往后移动一格。
# 此外因为p0 <= p1，在与p0的交换过程中，可能会把1换到i的位置，因此先做0 == i检测，再做一次1 == i检测
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l = len(nums)
        i = p0 = p1 = 0
        for i in range(l):
            if 0 == nums[i]:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 == p1: p1 += 1
                p0 += 1
            if 1 == nums[i]:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
        return

# # 方法二：首尾双指针;循环设计细节上比方法三要麻烦
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         l = len(nums)
#         i, p0, p2 = 0, 0, l-1
#         while i <= p2:
#             while i <= p2 and 2 == nums[i]:
#                 nums[i], nums[p2] = nums[p2], nums[i]
#                 p2 -= 1
#             if 0 == nums[i]:
#                 nums[i], nums[p0] = nums[p0], nums[i]
#                 p0 += 1
#             i += 1
#         return

# # 方法一：最容易想到的counter数字个数后排序
# from collections import Counter
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         dic = Counter(nums)
#         i = 0
#         for n in [0, 1, 2]:
#             for _ in range(dic[n]):
#                 nums[i] = n
#                 i += 1
#         return