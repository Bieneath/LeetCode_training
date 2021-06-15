# 不用在意折点在哪里，直接使用二分搜索！
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        le, ri = 0, len(nums)-1
        while le <= ri:
            mid = le + ri >> 1
            if nums[mid] == target:
                return mid
            if nums[le] <= nums[mid]: # 左侧升序
                if nums[le] <= target < nums[mid]:
                    ri = mid - 1
                else:
                    le = mid + 1
            else: # 右侧升序
                if nums[mid] < target < nums[le]:
                    le = mid + 1
                else:
                    ri = mid - 1
        return -1