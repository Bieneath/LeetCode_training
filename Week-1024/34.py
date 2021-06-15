# # 使用bisect
# import bisect
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         left = bisect.bisect_left(nums, target)
#         right = bisect.bisect_right(nums, target)
#         return [-1, -1] if left == right else [left, right - 1]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        def find_left(): # 找左边界的算法
            le, ri = 0, len(nums) - 1
            while le < ri:
                mid = (le + ri) >> 1
                if nums[mid] >= target:
                    ri = mid
                else:
                    le = mid + 1
            return le if nums[le] == target else -1
        def find_right(): # 找有边界的算法
            le, ri = 0, len(nums) - 1
            while le < ri:
                mid = (le + ri + 1) >> 1 # 和find_left对称的二分搜索，这里向上取整
                if nums[mid] <= target:
                    le = mid
                else:
                    ri = mid - 1
            return le if nums[le] == target else -1
        left = find_left()
        if -1 == left: return [-1, -1]
        right = find_right()
        return [left, right]